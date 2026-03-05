"""
test_synergy.py — Unit tests for src/core/synergy.py
"""

import asyncio
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from src.core.synergy import SynergyOperator


class TestSynergyOperator:
    def _make_operator(self):
        """Create a mock AutonomousOperator with required attributes."""
        op = MagicMock()
        op.link = MagicMock()
        op.recovery = MagicMock()
        op.web = MagicMock()
        op.web.run_cycle = AsyncMock()
        op.biz = MagicMock()
        op.guardian = MagicMock()
        op.audit = MagicMock()
        op.symphony = None
        return op

    def test_run_controlled_one_cycle(self):
        op = self._make_operator()
        synergy = SynergyOperator(op)

        asyncio.run(synergy.run_controlled(cycles=1))

        op.link.send_pulse.assert_called_once()
        op.recovery.run_cycle.assert_called_once()
        op.web.run_cycle.assert_called_once()
        op.biz.run_cycle.assert_called_once()
        op.guardian.run_cycle.assert_called_once()
        op.audit.run_cycle.assert_called_once()

    def test_run_controlled_multiple_cycles(self):
        op = self._make_operator()
        synergy = SynergyOperator(op)

        asyncio.run(synergy.run_controlled(cycles=3))

        assert op.link.send_pulse.call_count == 3
        assert op.recovery.run_cycle.call_count == 3
        assert op.audit.run_cycle.call_count == 3

    def test_symphony_conducted_when_present(self):
        op = self._make_operator()
        symphony = MagicMock()
        op.symphony = symphony
        synergy = SynergyOperator(op)

        asyncio.run(synergy.run_controlled(cycles=1))

        symphony.conduct_symphony.assert_called_once()

    def test_no_symphony_when_absent(self):
        op = self._make_operator()
        op.symphony = None
        synergy = SynergyOperator(op)

        # Should not raise
        asyncio.run(synergy.run_controlled(cycles=1))

    def test_heartbeat_pulse_content(self):
        op = self._make_operator()
        synergy = SynergyOperator(op)

        asyncio.run(synergy.run_controlled(cycles=1))

        call_kwargs = op.link.send_pulse.call_args.kwargs
        assert call_kwargs["pulse_type"] == "SYNERGY_HEARTBEAT"
        assert call_kwargs["node_name"] == "SynergyOrchestrator"
        assert call_kwargs["intensity"] == 1.0


class TestRunSynergy:
    def test_run_synergy_uses_default_base_dir(self):
        from src.core.synergy import run_synergy
        from src.config.settings import DAIOF_INSTALL_DIR

        mock_operator_class = MagicMock()
        mock_op = MagicMock()
        mock_op.link = MagicMock()
        mock_op.recovery = MagicMock()
        mock_op.web = MagicMock()
        mock_op.web.run_cycle = AsyncMock()
        mock_op.biz = MagicMock()
        mock_op.guardian = MagicMock()
        mock_op.audit = MagicMock()
        mock_op.symphony = None
        mock_operator_class.return_value = mock_op

        with patch("src.core.synergy._load_operator", return_value=mock_operator_class) as mock_load:
            asyncio.run(run_synergy(cycles=1))

        mock_load.assert_called_once_with(DAIOF_INSTALL_DIR)
        mock_op.recovery.run_cycle.assert_called_once()

    def test_run_synergy_with_custom_base_dir(self):
        from src.core.synergy import run_synergy

        mock_operator_class = MagicMock()
        mock_op = MagicMock()
        mock_op.link = MagicMock()
        mock_op.recovery = MagicMock()
        mock_op.web = MagicMock()
        mock_op.web.run_cycle = AsyncMock()
        mock_op.biz = MagicMock()
        mock_op.guardian = MagicMock()
        mock_op.audit = MagicMock()
        mock_op.symphony = None
        mock_operator_class.return_value = mock_op

        custom_dir = Path("/custom/path")
        with patch("src.core.synergy._load_operator", return_value=mock_operator_class) as mock_load:
            asyncio.run(run_synergy(base_dir=custom_dir, cycles=1))

        mock_load.assert_called_once_with(custom_dir)
