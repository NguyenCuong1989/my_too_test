"""
test_diagnostic.py — Unit tests for src/core/diagnostic.py
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from src.core.diagnostic import run_diagnostic


class TestRunDiagnostic:
    def _make_framework_mocks(self):
        """Return a tuple of mock classes to substitute for framework imports."""
        NeuralLink = MagicMock()
        link_instance = MagicMock()
        NeuralLink.return_value = link_instance

        SymphonyControlCenter = MagicMock()
        symphony_instance = MagicMock()
        SymphonyControlCenter.return_value = symphony_instance

        # Node mocks
        BizNode = MagicMock()
        GuardianNode = MagicMock()
        RecoveryNode = MagicMock()
        WebNode = MagicMock()
        AuditNode = MagicMock()

        return (
            NeuralLink,
            SymphonyControlCenter,
            BizNode,
            GuardianNode,
            RecoveryNode,
            WebNode,
            AuditNode,
            link_instance,
        )

    def test_returns_true_on_success(self):
        mocks = self._make_framework_mocks()
        with patch("src.core.diagnostic._load_framework", return_value=mocks[:7]):
            result = run_diagnostic(base_dir=Path("/fake/dir"))
        assert result is True

    def test_sends_diagnostic_pulse(self):
        mocks = self._make_framework_mocks()
        link_instance = mocks[7]
        with patch("src.core.diagnostic._load_framework", return_value=mocks[:7]):
            run_diagnostic(base_dir=Path("/fake/dir"))
        link_instance.send_pulse.assert_called_once_with(
            node_name="DiagnosticAgent",
            pulse_type="DIAGNOSTIC_INIT",
            content="Phase 1 Calibration Sequence",
            intensity=0.5,
        )

    def test_returns_false_when_framework_load_fails(self):
        with patch(
            "src.core.diagnostic._load_framework",
            side_effect=ImportError("no module"),
        ):
            result = run_diagnostic(base_dir=Path("/fake/dir"))
        assert result is False

    def test_returns_false_when_neural_link_init_fails(self):
        mocks = list(self._make_framework_mocks()[:7])
        mocks[0] = MagicMock(side_effect=RuntimeError("link error"))
        with patch("src.core.diagnostic._load_framework", return_value=mocks):
            result = run_diagnostic(base_dir=Path("/fake/dir"))
        assert result is False

    def test_returns_false_when_node_creation_fails(self):
        mocks = list(self._make_framework_mocks()[:7])
        mocks[2] = MagicMock(side_effect=RuntimeError("node error"))  # BizNode
        with patch("src.core.diagnostic._load_framework", return_value=mocks):
            result = run_diagnostic(base_dir=Path("/fake/dir"))
        assert result is False

    def test_uses_default_base_dir_when_none_provided(self):
        mocks = self._make_framework_mocks()
        with patch("src.core.diagnostic._load_framework", return_value=mocks[:7]) as mock_load:
            run_diagnostic()
        from src.config.settings import DAIOF_INSTALL_DIR
        mock_load.assert_called_once_with(DAIOF_INSTALL_DIR)

    def test_pulse_failure_still_returns_true(self):
        mocks = list(self._make_framework_mocks()[:7])
        link_instance = mocks[0].return_value
        link_instance.send_pulse.side_effect = RuntimeError("pulse error")
        with patch("src.core.diagnostic._load_framework", return_value=mocks):
            result = run_diagnostic(base_dir=Path("/fake/dir"))
        # Pulse failure is non-fatal — diagnostic still completes
        assert result is True
