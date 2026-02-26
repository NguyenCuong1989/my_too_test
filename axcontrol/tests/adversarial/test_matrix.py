import unittest
import time
from unittest.mock import MagicMock, patch

from core.loop.Van import ControlLoop
from core.Chinh.command import CommandEnvelope, CommandType, AtomicStep, AtomicStepType
from core.Chinh.policy import PolicyVerdict, PolicyOutcome
from core.Menh.stop_reasons import StopReason
from tests.adversarial.adversarial_env import AdversarialObserver

class TestAdversarialMatrix(unittest.TestCase):
    def setUp(self):
        self.loop = ControlLoop()
        self.adv_observer = AdversarialObserver()
        # Patch the real observer with our adversarial one
        self.patcher = patch('adapters.macos_ax.observer.observe', side_effect=self.adv_observer.observe)
        self.patcher.start()

        # Mock decision core
        self.loop.decision_core.evaluate_intent = MagicMock()

    def tearDown(self):
        self.patcher.stop()

    def _create_mock_cmd(self, steps_count=1):
        steps = [AtomicStep(type=AtomicStepType.AX_ACTION) for _ in range(steps_count)]
        envelope = CommandEnvelope(
            command_id="adv-cmd",
            intent_id="adv-intent",
            command_type=CommandType.CLICK,
            parameters={},
            normalized_state_hash="initial-hash",
            policy_context={},
            signature="sig",
            atomic_steps=steps
        )
        verdict = PolicyVerdict(outcome=PolicyOutcome.ALLOW, reason="adversarial-test")
        return envelope, verdict

    def test_sluggish_renderer_convergence(self):
        """Matrix Cell 1: UI settles eventually. Executor must wait."""
        # Scenario: Need 4 observations to settle
        self.adv_observer.set_scenario("sluggish", threshold=4)

        envelope, verdict = self._create_mock_cmd(steps_count=1)
        self.loop.decision_core.evaluate_intent.return_value = (envelope, verdict)

        start_ts = time.time()
        reason = self.loop.run_once()
        elapsed = time.time() - start_ts

        self.assertIsNone(reason)
        # Should have called observe multiple times (Settle by Convergence)
        self.assertGreaterEqual(self.adv_observer.call_count, 4)
        print(f"Sluggish Renderer settled in {elapsed:.2f}s after {self.adv_observer.call_count} calls")

    def test_ghost_mutation_detection(self):
        """Matrix Cell 2: UI changes unexpectedly. Must detect drift."""
        # Scenario: Mutant state appears after 1st emit
        self.adv_observer.set_scenario("ghost", trigger_at=5) # Trigger mid-loop

        envelope, verdict = self._create_mock_cmd(steps_count=1)
        self.loop.decision_core.evaluate_intent.return_value = (envelope, verdict)

        reason = self.loop.run_once()

        # In our implementation, run_once does a final drift check
        self.assertEqual(reason, StopReason.STATE_DRIFT_MID_STEP)
        print(f"Ghost Mutation detected: {reason}")

    def test_ax_stutter_recovery_or_fail(self):
        """Matrix Cell 4: AX Tree returns None. Must handle AX_LOST."""
        self.adv_observer.set_scenario("stutter", period=1) # Always None

        envelope, verdict = self._create_mock_cmd(steps_count=1)
        self.loop.decision_core.evaluate_intent.return_value = (envelope, verdict)

        reason = self.loop.run_once()
        self.assertEqual(reason, StopReason.AX_LOST)
        print(f"AX Stutter handled: {reason}")

    def test_narrow_interrupt_latency(self):
        """Matrix Cell 3: KillSwitch triggered mid-command."""
        # 10 steps command
        envelope, verdict = self._create_mock_cmd(steps_count=10)
        self.loop.decision_core.evaluate_intent.return_value = (envelope, verdict)

        # Trigger kill switch after 2 atomic steps
        # We hook into observe() or guard() to simulate async trigger
        original_guard = self.loop.watchdog.guard
        def mock_guard(start_ts, idx, engaged):
            if idx == 2:
                self.loop.kill_switch.trigger("Emergency")
            return original_guard(start_ts, idx, self.loop.kill_switch.engaged)

        self.loop.watchdog.guard = mock_guard

        reason = self.loop.run_once()

        self.assertEqual(reason, StopReason.KILL_SWITCH)
        # Check audit log step index
        last_record = self.loop.logger.sink.records[-1]
        self.assertEqual(last_record.step_index, 2)
        print(f"Narrow Interrupt caught at step {last_record.step_index}")

if __name__ == "__main__":
    unittest.main()
