import http.client
import json
import os
import tempfile
import threading
import unittest
from http.server import HTTPServer
from pathlib import Path


class BridgeNoDriftTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.log_path = Path(self._tmp.name) / "observe.ndjson"
        os.environ["AXCONTROL_SIM"] = "1"

        from core.bridge import http_server

        self.http_server = http_server
        self._start_server(self.log_path)

    def _start_server(self, audit_target: Path) -> None:
        os.environ["AXCONTROL_AUDIT_LOG"] = str(audit_target)
        # Use a dedicated bridge instance bound to this test's log path.
        self.http_server.bridge = self.http_server.Bridge()
        self.server = HTTPServer(("127.0.0.1", 0), self.http_server.Handler)
        self.port = self.server.server_port
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def _stop_server(self) -> None:
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)

    def _restart_server(self, audit_target: Path) -> None:
        self._stop_server()
        self._start_server(audit_target)

    def tearDown(self) -> None:
        self._stop_server()
        self._tmp.cleanup()
        os.environ.pop("AXCONTROL_AUDIT_LOG", None)

    def _post_chat(self, text: str) -> dict:
        conn = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        payload = json.dumps({"text": text})
        conn.request(
            "POST", "/chat", body=payload, headers={"Content-Type": "application/json"}
        )
        res = conn.getresponse()
        body = res.read()
        conn.close()
        self.assertEqual(res.status, 200)
        return json.loads(body)

    def test_same_input_same_hash_and_log_growth(self) -> None:
        r1 = self._post_chat("status?")
        r2 = self._post_chat("status?")

        self.assertTrue(r1["audit"]["recorded"])
        self.assertTrue(r2["audit"]["recorded"])
        self.assertEqual(r1["audit"]["Chung"], r2["audit"]["Chung"])

        lines = self.log_path.read_text(encoding="utf-8").strip().splitlines()
        self.assertEqual(len(lines), 2)
        records = [json.loads(line) for line in lines]
        self.assertTrue(all(rec.get("type") == "bridge_audit" for rec in records))
        self.assertEqual(records[0]["Chung"], records[1]["Chung"])

    def test_different_input_different_hash(self) -> None:
        r1 = self._post_chat("status?")
        r2 = self._post_chat("/cli pwd")

        self.assertTrue(r1["audit"]["recorded"])
        self.assertTrue(r2["audit"]["recorded"])
        self.assertNotEqual(r1["audit"]["Chung"], r2["audit"]["Chung"])

        lines = self.log_path.read_text(encoding="utf-8").strip().splitlines()
        self.assertEqual(len(lines), 2)
        records = [json.loads(line) for line in lines]
        self.assertNotEqual(records[0]["Chung"], records[1]["Chung"])

    def test_audit_write_failure_sets_explicit_stop_reason(self) -> None:
        bad_target = Path(self._tmp.name) / "audit_dir"
        bad_target.mkdir(parents=True, exist_ok=True)
        self._restart_server(bad_target)

        resp = self._post_chat("status?")
        self.assertFalse(resp["audit"]["recorded"])
        self.assertEqual(resp["stop"]["reason"], "audit_write_failed")
        self.assertIn("error", resp["audit"])
        self.assertTrue(bad_target.is_dir())
        self.assertEqual(list(bad_target.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
