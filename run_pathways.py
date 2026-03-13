import os
import json
import subprocess
import time

def log_header(title):
    print("\n" + "="*80)
    print(f"🔄 ĐANG KÍCH HOẠT: {title}")
    print("="*80)

def run_omni(skill, payload):
    print(f"  [>] Điều phối {skill} với payload: {payload}")
    cmd = ["/Users/andy/my_too_test/omni", skill, json.dumps(payload)]
    env = os.environ.copy()
    env["PYTHONPATH"] = f"/Users/andy/my_too_test:{env.get('PYTHONPATH', '')}"
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=30, env=env)
        print(f"  [<] Kết quả (STDOUT): {out.stdout.strip()}")
        if out.stderr.strip():
            print(f"  [!] Lỗi (STDERR): {out.stderr.strip()}")
        return out.stdout.strip()
    except subprocess.TimeoutExpired:
        print(f"  [!] Hết thời gian chờ (Timeout)")
        return "TIMEOUT"
    except Exception as e:
        print(f"  [!] Lỗi hệ thống: {e}")
        return "ERROR"

def run_pathways():
    # PATHWAY 1: BizNode & Data Flow
    log_header("Pathway 1: Business & Memory (O.P 1)")
    run_omni("biz_node", {"action": "check_status"})
    run_omni("redis_agent", {"action": "ping"})
    run_omni("postgres_agent", {"query": "SELECT 1;"})

    # PATHWAY 2: Security & Guardian
    log_header("Pathway 2: Security & Guardian (O.P 2)")
    run_omni("audit_node", {"target": "system"})
    run_omni("guardian_node", {"target": "health_check"})

    # PATHWAY 3: Multi-Agent Council
    log_header("Pathway 3: Phoenix Council & Planners (O.P 3)")
    print("  [>] Executing standalone Multi-Agent loop from /Users/andy/my_too_test/apo_adaptive_planner.py")
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = f"/Users/andy/my_too_test:{env.get('PYTHONPATH', '')}"
        out = subprocess.run(["python3", "/Users/andy/my_too_test/apo_adaptive_planner.py", "run_loop"], capture_output=True, text=True, timeout=30, env=env)
        for line in out.stdout.split('\n'):
            if line.strip():
                print(f"  [Σ] {line}")
    except Exception as e:
        print(f"  [!] Council execution error: {e}")

    # PATHWAY 4: Physical Control (AX)
    log_header("Pathway 4: Physical Control (O.P 4 - SEALED AREA)")
    print("  [>] Thẩm định Agent điều khiển UI...")
    run_omni("agent_browser_v2", {"action": "status"})

    print("\n" + "="*80)
    print("🏁 TẤT CẢ PATHWAYS KIỂM TOÁN ĐÃ HOÀN TẤT.")
    print("="*80)

if __name__ == "__main__":
    run_pathways()
