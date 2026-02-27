import os
import logging
import subprocess
import json
import sys
from pathlib import Path

try:
    from .config import BASE_DIR
    from .neural_link import NeuralLink
except (ImportError, ValueError):
    sys.path.append(str(Path(__file__).parent.parent))
    from config import BASE_DIR
    from neural_link import NeuralLink

class GuardianNode:
    def __init__(self):
        self.logger = logging.getLogger("GuardianNode")
        self.repo_path = BASE_DIR / "DAIOF-Framework"
        self.link = NeuralLink()

    def run_cycle(self):
        self.logger.info("Guardian sweeping for anomalies...")
        self.cleanup_github_issues()
        self.check_system_health()

    def cleanup_github_issues(self):
        """Dọn dẹp các issue rác do bot tạo ra"""
        try:
            # Sử dụng gh CLI nếu có
            cmd = ["gh", "issue", "list", "--repo", "NguyenCuong1989/DAIOF-Framework", "--json", "number,title"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                issues = json.loads(result.stdout)
                for issue in issues:
                    if "EMERGENCY" in issue['title'] or "CI/CD Failure" in issue['title']:
                        self.logger.info(f"Closing spam issue: {issue['number']}")
                        subprocess.run(["gh", "issue", "close", str(issue['number']), "--repo", "NguyenCuong1989/DAIOF-Framework"])
                        self.link.log_service_event(
                            service="GuardianService",
                            e_type="TASK_HANDOVER",
                            content=f"Closed spam issue #{issue['number']}: {issue['title']}"
                        )
        except Exception as e:
            self.logger.error(f"GitHub cleanup error: {e}")

    def check_system_health(self):
        """Kiểm tra Docker và các dịch vụ quan trọng"""
        try:
            # Check docker containers
            cmd = ["docker", "ps", "--format", "{{.Names}}"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                containers = result.stdout.strip().split('\n')
                self.logger.info(f"Running containers: {', '.join(containers)}")
                self.link.log_service_event(
                    service="GuardianService",
                    e_type="STATUS",
                    content=f"System health check passed. Running containers: {len(containers)}",
                    meta=json.dumps({"containers": containers})
                )
            else:
                self.logger.warning("Docker daemon might be down.")
                self.link.log_service_event(
                    service="GuardianService",
                    e_type="SLA_BREACH",
                    content="Docker daemon might be down or unreachable."
                )
        except Exception as e:
            self.logger.error(f"Health check error: {e}")
            self.link.log_service_event(
                service="GuardianService",
                e_type="SLA_BREACH",
                content=f"Health check execution error: {str(e)[:200]}"
            )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    node = GuardianNode()
    node.run_cycle()
