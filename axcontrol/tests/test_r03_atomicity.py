import unittest
import time
from unittest.mock import MagicMock

from core.loop.Van import ControlLoop
from core.Chinh.command import CommandEnvelope, CommandType, AtomicStep, AtomicStepType
from core.Chinh.policy import PolicyVerdict, PolicyOutcome
from core.Menh.stop_reasons import StopReason

class TestR03Atomicity(unittest.TestCase):
    def setUp(self):
        self.loop = ControlLoop()
        # Mock decision core to return a multi-step command
        self.loop.decision_core.evaluate_intent = MagicMock()

        # Mock observer and settle to provide stability
        self.loop._settle = MagicMock(return_value="stable-hash")

        from adapters.macos_ax.observer import Snapshot
        dummy_snap = Snapshot(app="Finder", role="AXWindow", label="Test", bbox=(0,0,10,10))
        import adapters.macos_ax.observer as observer
        observer.observe = MagicMock(return_value=dummy_snap)

    def test_atomic_execution_and_chain(self):
        """Verify that a 3-step command produced 3 audit records with chained hashes."""
        steps = [
            AtomicStep(type=AtomicStepType.KEY_DOWN, parameters={"key": "TAB"}),
            AtomicStep(type=AtomicStepType.KEY_UP, parameters={"key": "TAB"}),
            AtomicStep(type=AtomicStepType.WAIT_SETTLE, parameters={"ms": 100})
        ]

        mock_envelope = CommandEnvelope(
            command_id="cmd-123",
            intent_id="intent-123",
            command_type=CommandType.CLICK,
            parameters={},
            normalized_state_hash="initial-hash",
            policy_context={},
            signature="sig-123",
            atomic_steps=steps
        )
        mock_verdict = PolicyVerdict(outcome=PolicyOutcome.ALLOW, reason="test")

        self.loop.decision_core.evaluate_intent.return_value = (mock_envelope, mock_verdict)

        # Run one loop iteration
        self.loop.run_once()

        # Verify Audit Log
        records = self.loop.logger.sink.records
        self.assertEqual(len(records), 3)

        # Check chaining
        for i in range(len(records)):
            self.assertEqual(records[i].step_index, i)
            if i > 0:
                self.assertEqual(records[i].chained_hash, records[i-1].Chung)
                print(f"Step {i} chained correctly to Step {i-1}")

    def test_kill_switch_interrupt(self):
        """Verify that KillSwitch stops execution mid-command."""
        steps = [AtomicStep(type=AtomicStepType.AX_ACTION) for _ in range(10)]

        mock_envelope = CommandEnvelope(
            command_id="cmd-kill",
            intent_id="intent-kill",
            command_type=CommandType.CLICK,
            parameters={},
            normalized_state_hash="initial-hash",
            policy_context={},
            signature="sig-kill",
            atomic_steps=steps
        )
        mock_verdict = PolicyVerdict(outcome=PolicyOutcome.ALLOW, reason="test")
        self.loop.decision_core.evaluate_intent.return_value = (mock_envelope, mock_verdict)

        # Trigger kill switch after 2 steps (simulated by mocking watchdog or executor)
        # For simplicity, we trigger it manually before run
        # In a real race, it would be triggered asynchronously

        original_guard = self.loop.watchdog.guard
        def mock_guard(start_ts, event_count, kill_engaged):
            if event_count == 3:
                self.loop.kill_switch.trigger("human emergency")
            return original_guard(start_ts, event_count, self.loop.kill_switch.engaged)

        self.loop.watchdog.guard = mock_guard

        reason = self.loop.run_once()

        self.assertEqual(reason, StopReason.KILL_SWITCH)
        records = self.loop.logger.sink.records
        # Should have N records before kill + 1 record for the stop
        print(f"Execution stopped at step {records[-1].step_index} with reason {reason}")

if __name__ == "__main__":
    unittest.main()
