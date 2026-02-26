# Mock File for PoC Auto-Fix
import sys
from core.Chung.log_schema import AuditRecord
from core.Chung.logger import AuditLogger

class MockLoop:
    def __init__(self):
        self.logger = AuditLogger()

loop = MockLoop()
def mock_cli_loop():
    rc = 0
    out = "success"
    err = ""
    cmd = "ls"

    # Needs to be replaced by the Ops Agent
    loop.logger.log(AuditRecord(timestamp=0, state_before={}, intent={"source": "cli"}, command={"cmd": cmd}, policy_decision={}, state_after={}, Chung="cli-output", stop_reason=None))
                    print(f"tool[cli] exit={rc}\n{out}{err}")

    print("cancelled")

if __name__ == "__main__":
    mock_cli_loop()
