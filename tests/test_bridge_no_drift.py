import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]


class BridgeNoDriftTests(unittest.TestCase):
    def test_sigma_cos_runtime_surface_exists(self):
        required = [
            ROOT / "sigma-cos" / "docker-compose.yml",
            ROOT / "sigma-cos" / "services" / "mcp-router" / "server.js",
            ROOT / "sigma-cos" / "services" / "factory-worker" / "main.py",
            ROOT / "sigma-cos" / "services" / "ai-sidecar" / "main.py",
            ROOT / "sigma-cos" / "tests" / "smoke.sh",
        ]
        missing = [str(p.relative_to(ROOT)) for p in required if not p.is_file()]
        self.assertEqual(missing, [], f"runtime surface drift: missing {missing}")

    def test_no_workflow_points_at_removed_axcontrol_root(self):
        workflows = ROOT / ".github" / "workflows"
        offenders = []
        for path in workflows.glob("*.yml"):
            content = path.read_text(encoding="utf-8")
            if "working-directory: axcontrol" in content:
                offenders.append(str(path.relative_to(ROOT)))
        self.assertEqual(offenders, [], f"workflow path drift: {offenders}")


if __name__ == "__main__":
    unittest.main()
