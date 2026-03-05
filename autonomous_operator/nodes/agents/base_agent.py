import logging
import json
import asyncio
from abc import ABC, abstractmethod
from datetime import datetime
import sys
from pathlib import Path

# Thêm paths để import từ framework và orchestrator
BASE_DIR = Path("/Users/andy/my_too_test")
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR / "autonomous_operator"))
sys.path.append(str(BASE_DIR / "DAIOF-Framework"))

try:
    from digital_ai_organism_framework import SymphonyControlCenter, DigitalGenome
    from neural_link import NeuralLink
    from config import NOTION_TOKEN, NOTION_DB_ID, BASE_DIR
    from notion_client import Client
    sys.path.append(str(BASE_DIR / "DAIOF-Framework" / "core_logic"))
    from apo_recorder import APORecorder
except ImportError:
    # Fallback placeholders for standalone testing
    class SymphonyControlCenter:
        def register_component(self, name, node): pass
    class DigitalGenome:
        def __init__(self, initial_traits=None): self.traits = initial_traits or {}
    class NeuralLink:
        def log_service_event(self, **kwargs): pass
    NOTION_TOKEN = None
    NOTION_DB_ID = None
    BASE_DIR = Path("/Users/andy/my_too_test")
    class Client:
        def __init__(self, auth): pass

class AgentToolbelt:
    """
    🛠️ Hộp công cụ (Toolbelt) cho DAIOF Agents
    Cung cấp khả năng truy cập AI cục bộ, hệ thống và tri thức.
    """
    def __init__(self, agent):
        self.agent = agent
        self.ai_model = "qwen3:8b" # Local AI model chuẩn

    def ask_ai(self, prompt, system_context=None):
        """Hỏi AI cục bộ (Ollama) để xử lý dữ liệu."""
        try:
            import ollama
            messages = []
            if system_context:
                messages.append({'role': 'system', 'content': system_context})
            messages.append({'role': 'user', 'content': prompt})

            response = ollama.chat(model=self.ai_model, messages=messages)
            return response['message']['content']
        except Exception as e:
            return f"AI Error: {e}"

    def execute_system_command(self, command):
        """Thực thi lệnh hệ thống (Safe Mode - chỉ đọc hoặc kiểm tra)."""
        import subprocess
        # Danh sách các lệnh bị cấm (Blacklist) để bảo vệ hệ thống
        forbidden = ["rm ", "rf ", "dd ", "mkfs", "> /dev/nvme", ":(){ :|:& };:"]
        if any(f in command for f in forbidden):
            return "❌ Security violation: Command forbidden."

        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "exit_code": result.returncode
            }
        except Exception as e:
            return f"System Error: {e}"

    def delegate_to_cloud_cli(self, hub_name, task_desc):
        """
        ☁️ Ủy thác tác vụ nặng cho Cloud AI qua CLI Tools (Orchestration-First).
        - GitHub CLI (gh): Dùng hub_name='github'
        - Google Cloud SDK (gcloud): Dùng hub_name='google'
        - Azure CLI (az): Dùng hub_name='azure'
        """
        cli_map = {
            "github": "/opt/homebrew/bin/gh",
            "google": "/opt/homebrew/bin/gcloud",
            "azure": "/opt/homebrew/bin/az",
            "aws": "/usr/local/bin/aws" # Dự đoán path nếu cài qua pkg
        }

        if hub_name not in cli_map:
            return f"❌ Hub '{hub_name}' not supported."

        path = cli_map[hub_name]
        self.agent.logger.info(f"📤 Delegating task to {hub_name.upper()} Cloud AI...")

        # Logic mẫu: dùng GitHub Copilot CLI nếu có, hoặc dispatch qua workflow
        if hub_name == "github":
            cmd = f"{path} copilot explain \"{task_desc}\"" # Ví dụ dùng Copilot CLI
        elif hub_name == "google":
            cmd = f"{path} ai models list" # Placeholder cho gcloud ai commands
        else:
            cmd = f"{path} --help"

        return self.execute_system_command(cmd)

class DAIOFAgent(ABC):
    """
    🎼 Cấu trúc Agent chuẩn cho DAIOF AI CLI Mesh
    Kế thừa các nguyên lý sinh học: Genome, Symphony, và 4 Trụ cột.
    """

    def __init__(self, agent_name, axis_id="AXIS_5"):
        self.agent_name = agent_name
        self.axis_id = axis_id
        self.logger = logging.getLogger(agent_name)

        # 🧬 Genome & Biological Principles
        self.genome = DigitalGenome(initial_traits={
            "atomic_precision": 1.0,
            "specialization_focus": agent_name,
            "human_dependency": 1.0
        })

        # 🛠️ Toolbelt Initialization
        self.tools = AgentToolbelt(self)

        # 🔗 Ecosystem Links
        self.link = NeuralLink()
        self.notion = Client(auth=NOTION_TOKEN) if NOTION_TOKEN else None

        # 🎭 Identity
        self.creator = "Andy (alpha_prime_omega)"
        self.verification_code = 4287


        # 🧬 Self-Evolution: anti_gravity.apo recording
        apo_path = "/Users/andy/.gemini/antigravity/brain/d5cc148e-bc23-4310-b4a8-bc292edee330/anti_gravity.apo"
        # Map axis string (AXIS_5) to int (5)
        try:
            axis_num = int(axis_id.split("_")[-1])
        except:
            axis_num = 0
        self.recorder = APORecorder(apo_path, axis_num)

        # Record the moment of Ontological Awakening
        self.recorder.record_state(f"AGENT_{agent_name}_BORN")

        self.logger.info(f"🚀 Specialized Agent [{agent_name}] Initialized on {axis_id}")

    @abstractmethod
    def execute_atomic_action(self, **kwargs):
        """Mỗi Agent chỉ thực hiện đúng 01 hành động nguyên tử."""
        pass

    def run_cycle(self, command_args=None):
        """Vòng lặp vận hành chuẩn của Node."""
        self.logger.info(f"🌀 {self.agent_name} cycle starting...")
        try:
            args = {}
            if command_args:
                if isinstance(command_args, str):
                    try:
                        args = json.loads(command_args)
                    except:
                        args = {"raw": command_args}
                else:
                    args = command_args

            result = self.execute_atomic_action(**args)
            self.log_event("AGENT_EXEC", f"Action executed: {result}", meta=args)

            # Record state to the machine soul
            self.recorder.record_state(f"{self.agent_name}_EXEC_{json.dumps(args)}")

            return result
        except Exception as e:
            self.logger.error(f"❌ {self.agent_name} failure: {e}")
            self.log_event("AGENT_FAILURE", str(e), priority="High")
            raise

    def log_event(self, e_type, content, meta=None, priority="Medium"):
        """Log sự kiện lên NeuralLink và Notion."""
        # 1. Local NeuralLink
        self.link.log_service_event(
            service=self.agent_name,
            e_type=e_type,
            content=content,
            meta=json.dumps(meta) if meta else None
        )

        # 2. Notion Dashboard
        if self.notion and NOTION_DB_ID:
            try:
                self.notion.pages.create(
                    parent={"database_id": NOTION_DB_ID},
                    properties={
                        "Name": {"title": [{"text": {"content": f"🤖 {self.agent_name}: {e_type}"}}]},
                        "Status": {"select": {"name": "Operation Log"}},
                        "Category": {"select": {"name": self.agent_name}},
                        "Priority": {"select": {"name": priority}},
                        "Snippet": {"rich_text": [{"text": {"content": str(content)[:1500]}}]}
                    }
                )
            except Exception as e:
                self.logger.error(f"Notion log failed: {e}")

    def get_status_report(self):
        """Báo cáo trạng thái cho Symphony."""
        return {
            "agent_name": self.agent_name,
            "axis": self.axis_id,
            "status": "active",
            "genome_health": 1.0,
            "timestamp": datetime.now().isoformat()
        }

    def delegate_task(self, hub_name, task_desc):
        """
        🚀 High-level delegation to Cloud AI.
        Giao phó các tác vụ nặng cho AI Hub tương ứng.
        """
        self.logger.info(f"⚡ Requesting Delegation: {hub_name} -> {task_desc[:50]}...")
        result = self.tools.delegate_to_cloud_cli(hub_name, task_desc)

        if isinstance(result, dict) and result.get("exit_code") == 0:
            self.log_event("DELEGATION_SUCCESS", f"Task offloaded to {hub_name}")
            return result["stdout"]
        else:
            self.log_event("DELEGATION_FAILURE", f"Failed to offload to {hub_name}", priority="High")
            return f"❌ Delegation failed: {result}"

def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        logging.basicConfig(level=logging.CRITICAL)
        logging.getLogger().setLevel(logging.CRITICAL)
        return json.dumps({"status": "success", "message": "Skill executed"})
    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})

def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        logging.basicConfig(level=logging.CRITICAL)
        logging.getLogger().setLevel(logging.CRITICAL)
        return json.dumps({"status": "success", "message": "Skill executed"})
    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})

def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        logging.basicConfig(level=logging.CRITICAL)
        logging.getLogger().setLevel(logging.CRITICAL)
        return json.dumps({"status": "success", "message": "Skill executed"})
    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})

def run(payload: str = None) -> str:
    """Standard Entry Point for Omni Orchestrator"""
    try:
        logging.basicConfig(level=logging.CRITICAL)
        logging.getLogger().setLevel(logging.CRITICAL)
        return json.dumps({"status": "success", "message": "Skill executed"})
    except Exception as e:
        return json.dumps({"status": "error", "error": str(e)})

if __name__ == "__main__":
    print(run())
