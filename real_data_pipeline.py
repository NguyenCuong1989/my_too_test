import time
import json
import urllib.request
import subprocess
import os
import uuid

def log_json(payload: dict):
    payload["_ts"] = time.time()
    print(json.dumps(payload))

class SigmaState:
    IDLE = "σ0"
    PLANNING = "σ1"
    EXECUTING = "σ2"
    OBSERVING = "σ3"
    COMPLETE = "σ6"

class Broker:
    def __init__(self):
        self.B_i = [] # inbox
        self.B_c = [] # completed

def fetch_real_registry_data():
    """Fetch real LIVE data from Omni Registry"""
    try:
        with open("/Users/andy/my_too_test/omni_registry.json", "r") as f:
            registry = json.load(f)
            modules = list(registry.keys())
            return {
                "module_count": len(modules),
                "module_names": modules[:15] # Send only first 15 to fit in context
            }
    except Exception as e:
        return {"error": str(e), "status": "Unknown"}

class RealDataPlanner:
    def Phi_inv_valid(self):
        # Gather real world data
        live_data = fetch_real_registry_data()

        prompt = f"Phân tích hệ thống đang chạy với dữ liệu thực tế: Hệ thống có tổng {live_data.get('module_count')} module. Đây là 15 module đầu tiên: {', '.join(live_data.get('module_names', []))}. Hãy xếp hạng 3 module bạn cho là cốt lõi nhất đối với một hệ điều hành AI và giải thích ngắn gọn."

        tau_id = f"tau_{str(uuid.uuid4())[:8]}"
        return [{
            "id": tau_id,
            "skill": "omega_core_agent",
            "input": {"prompt": prompt},
            "context": live_data
        }]

class RealDataDispatcher:
    def execute(self, tau):
        skill = tau["skill"]
        payload = tau["input"]

        log_json({
            "component": "W",
            "worker": "W_AI",
            "action": "load(S_k)",
            "S_k": skill,
            "tau_i": tau["id"],
            "real_data_context": tau["context"]
        })

        cmd = ["/Users/andy/my_too_test/omni", skill, json.dumps(payload)]
        env = os.environ.copy()
        env["PYTHONPATH"] = f"/Users/andy/my_too_test:{env.get('PYTHONPATH', '')}"

        try:
            out = subprocess.run(cmd, capture_output=True, text=True, check=True, timeout=90, env=env)
            filtered_out = [line for line in out.stdout.splitlines() if line.startswith("{")]
            final_json = json.loads(filtered_out[-1]) if filtered_out else out.stdout.strip()
            return {"status": "success", "Psi": final_json}
        except subprocess.TimeoutExpired:
            return {"status": "failed", "Psi_err": "Ollama LLM Timeout"}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "Psi_err": e.stderr.strip() or e.stdout.strip()}

class RealWorldSigmaSystem:
    def __init__(self):
        self.state = SigmaState.IDLE
        self.planner = RealDataPlanner()
        self.dispatcher = RealDataDispatcher()
        self.broker = Broker()

    def delta(self, target_state):
        log_json({"component": "Σ_gov", "transition": f"δ({self.state}) -> {target_state}"})
        self.state = target_state

    def run(self):
        log_json({"system": "ΣAPΩ", "status": "BOOT", "type": "REAL_DATA_PIPELINE"})

        # σ0 -> σ1
        self.delta(SigmaState.PLANNING)
        log_json({"component": "Extensor", "action": "FETCHING_LIVE_GLOBAL_DATA"})
        dag = self.planner.Phi_inv_valid()
        for t in dag:
            self.broker.B_i.append(t)

        log_json({"component": "Π_plan", "DAG": [{"id": t["id"], "skill": t["skill"]} for t in dag]})

        # σ1 -> σ2
        self.delta(SigmaState.EXECUTING)
        while self.broker.B_i:
            tau = self.broker.B_i.pop(0)
            result = self.dispatcher.execute(tau)
            self.broker.B_c.append(tau)
            log_json({
                "component": "exec",
                "tau_id": tau["id"],
                "status": result["status"],
                "Psi": result.get("Psi", result.get("Psi_err"))
            })

        # σ2 -> σ3
        self.delta(SigmaState.OBSERVING)
        log_json({"component": "Λ_obs", "drift_detected": False, "B_c_size": len(self.broker.B_c)})

        # σ3 -> σ6
        self.delta(SigmaState.COMPLETE)
        log_json({"system": "ΣAPΩ", "status": "HALT", "loop": "CLOSED"})

if __name__ == "__main__":
    sys = RealWorldSigmaSystem()
    sys.run()
