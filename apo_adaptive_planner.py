import os
import uuid
import json
import subprocess
import time

def log_json(payload: dict):
    payload["_ts"] = time.time()
    print(json.dumps(payload))

class SigmaState:
    IDLE = "σ0"
    PLANNING = "σ1"
    EXECUTING = "σ2"
    OBSERVING = "σ3"
    DRIFT = "σ4"
    HEAL = "σ5"
    COMPLETE = "σ6"

class Broker:
    def __init__(self):
        self.B_i = [] # inbox
        self.B_p = [] # processing
        self.B_c = [] # completed
        self.B_f = [] # failed

class PlannerEngine:
    def Phi_inv_valid(self, H_t):
        """Π_plan = Φ⁻¹_valid(R) -> DAG"""
        tau_id = f"tau_{str(uuid.uuid4())[:8]}"
        return [{
            "id": tau_id,
            "skill": "audit_node",
            "input": {"target": "system"}
        }]

class OrchestratorDispatcher:
    def __init__(self):
        self.W = ["W_1"] # W_j

    def dispatch(self, tau, broker: Broker):
        """Π_dispatch = τ_i -> B"""
        broker.B_i.remove(tau)
        broker.B_p.append(tau)
        return self.W[0]

    def execute(self, tau, worker_j):
        """W_j : load(S_k) -> exec(τ_i) -> log(Ψ)"""
        skill = tau["skill"] # S_k
        payload = tau["input"]

        log_json({
            "component": "W",
            "worker": worker_j,
            "action": "load(S_k)",
            "S_k": skill,
            "tau_i": tau["id"]
        })

        cmd = ["/Users/andy/my_too_test/omni", skill, json.dumps(payload)]
        env = os.environ.copy()
        env["PYTHONPATH"] = f"/Users/andy/my_too_test:{env.get('PYTHONPATH', '')}"

        try:
            out = subprocess.run(cmd, capture_output=True, text=True, check=True, env=env)
            # Normalize to pure json
            return {"status": "success", "Psi": json.loads(out.stdout.strip()) if out.stdout.strip().startswith("{") else out.stdout.strip()}
        except subprocess.CalledProcessError as e:
            return {"status": "failed", "Psi_err": e.stderr.strip()}

class APOSigmaKernel:
    def __init__(self):
        self.state = SigmaState.IDLE
        self.planner = PlannerEngine()
        self.dispatcher = OrchestratorDispatcher()
        self.broker = Broker()

    def delta(self, target_state):
        log_json({
            "component": "Σ_gov",
            "transition": f"δ({self.state}) -> {target_state}"
        })
        self.state = target_state

    def run(self):
        log_json({"system": "ΣAPΩ", "status": "BOOT", "components": ["Ω", "K", "B", "W", "S", "D", "M", "I"]})

        while True:
            if self.state == SigmaState.IDLE: # σ0
                self.delta(SigmaState.PLANNING) # δ(σ0) → σ1

            elif self.state == SigmaState.PLANNING: # σ1
                dag = self.planner.Phi_inv_valid({"tick": time.time()})
                for tau in dag:
                    self.broker.B_i.append(tau)
                log_json({"component": "Π_plan", "DAG": dag, "B_inbox_size": len(self.broker.B_i)})
                self.delta(SigmaState.EXECUTING) # δ(σ1) → σ2

            elif self.state == SigmaState.EXECUTING: # σ2
                while self.broker.B_i:
                    tau = self.broker.B_i[0]
                    worker_j = self.dispatcher.dispatch(tau, self.broker)
                    log_json({"component": "Π_dispatch", "tau": tau["id"], "worker": worker_j})

                    result = self.dispatcher.execute(tau, worker_j)

                    if result["status"] == "success":
                        self.broker.B_c.append(tau)
                    else:
                        self.broker.B_f.append(tau)

                    self.broker.B_p.remove(tau)
                    log_json({
                        "component": "exec",
                        "tau": tau["id"],
                        "result": result["status"],
                        "Psi": result.get("Psi") or result.get("Psi_err")
                    })

                self.delta(SigmaState.OBSERVING) # δ(σ2) → σ3

            elif self.state == SigmaState.OBSERVING: # σ3
                drift = len(self.broker.B_f) > 0

                log_json({
                    "component": "Λ_obs",
                    "metrics": "Π_metrics",
                    "logs": "Π_logs",
                    "B_c_size": len(self.broker.B_c),
                    "B_f_size": len(self.broker.B_f),
                    "drift_detected": drift
                })

                if drift:
                    self.delta(SigmaState.DRIFT) # δ(σ3) → σ4
                else:
                    self.delta(SigmaState.COMPLETE) # δ(σ3) → σ6

            elif self.state == SigmaState.DRIFT: # σ4
                log_json({"component": "Σ_gov", "status": "DRIFT_RESOLUTION_STARTED"})
                self.delta(SigmaState.HEAL) # δ(σ4) → σ5

            elif self.state == SigmaState.HEAL: # σ5
                # Simple healing logic for demonstration (clear failed buffer)
                self.broker.B_f.clear()
                self.delta(SigmaState.EXECUTING) # δ(σ5) → σ2

            elif self.state == SigmaState.COMPLETE: # σ6
                log_json({"system": "ΣAPΩ", "status": "HALT", "loop": "CLOSED"})
                break

if __name__ == "__main__":
    import sys
    # If run in loop mode as the core component
    kernel = APOSigmaKernel()
    kernel.run()
