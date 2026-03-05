# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import json
import os
import subprocess
from pathlib import Path
from autonomous_operator.gemini_orchestrator import GeminiOrchestrator

inbox = Path('factory/inbox')
orc = GeminiOrchestrator()

for task_file in inbox.glob('*.task'):
    with open(task_file, 'r') as f:
        task = json.load(f)

    try:
        module = orc.resolve_module(task['skill_name'])
        plan = orc.create_execution_plan(task, module)
        res = orc.execute_plan(plan)
        orc.store_result(res)
        os.remove(task_file)
    except Exception as e:
        print(f"Failed {task_file}: {e}")
