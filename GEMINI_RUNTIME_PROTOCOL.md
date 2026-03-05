GEMINI_RUNTIME_PROTOCOL.md

Protocol vận hành cho Gemini CLI trong hệ thống đa module

⸻

0. PURPOSE

Protocol này định nghĩa cách Gemini CLI vận hành như một orchestrator để:
	•	quét toàn bộ hệ thống
	•	hiểu cấu trúc module
	•	xây dựng capability graph
	•	điều phối các module
	•	thực thi task một cách an toàn và có kiểm soát

Gemini không phải worker.
Gemini đóng vai trò:

Planner
Resolver
Dispatcher
Validator


⸻

1. SYSTEM PRINCIPLE

Gemini phải tuân thủ các nguyên tắc sau:

1. Scan before execution
2. Resolve module before run
3. Never execute unknown code
4. Always log execution
5. Fail closed on error


⸻

2. SYSTEM LAYERS

Hệ thống được chia thành 4 lớp.

LAYER 1
Filesystem

LAYER 2
Module registry

LAYER 3
Execution orchestration

LAYER 4
Execution engine


⸻

3. FILESYSTEM SCAN PHASE

Gemini phải scan toàn bộ repository trước khi thực thi task.

Scan bao gồm:

source code
scripts
configs
tests
runtime folders

Scan command:

tree -L 6

hoặc

find . -type f

Output phải tạo:

SYSTEM_FILE_INDEX.json

Ví dụ:

{
 "path": "factory/factory_worker.py",
 "type": "python",
 "category": "execution_engine"
}


⸻

4. FILE CLASSIFICATION

Gemini phân loại file theo pattern.

Rules:

core/*.py → system logic
factory/*.py → execution engine
autonomous_operator/*.py → orchestration
tests/*.py → validation
*.json → configuration
*.sh → runtime script
logs/* → runtime artifacts

Gemini phải tạo:

SYSTEM_MODULE_CATALOG.json


⸻

5. SEMANTIC INDEXING

Gemini đọc nội dung file để phát hiện:

functions
classes
entry points
execution hooks

Ví dụ:

def execute_task()

Gemini ghi nhận capability:

{
 "module": "factory_worker",
 "capability": "task_execution"
}


⸻

6. CAPABILITY GRAPH

Gemini xây dựng graph chức năng của hệ.

Ví dụ:

orchestrator
    │
    ├─ factory_worker
    │       │
    │       ├─ script_runner
    │       └─ docker_runner
    │
    └─ core_tools
            │
            ├─ browser
            └─ navigation

Graph lưu tại:

SYSTEM_CAPABILITY_GRAPH.json


⸻

7. MODULE REGISTRY

Gemini phải duy trì registry module.

Ví dụ:

{
 "browser_automation": "core/browser",
 "task_execution": "factory/factory_worker.py",
 "orchestration": "autonomous_operator/apoct_orchestrator.py"
}

File:

SYSTEM_MODULE_REGISTRY.json


⸻

8. TASK INTAKE

Task có thể đến từ:

CLI command
factory/inbox/
API request
event trigger

Ví dụ:

factory/inbox/task.json

Task structure:

{
 "task_id": "123",
 "type": "scrape_website",
 "parameters": {...}
}


⸻

9. TASK RESOLUTION

Gemini resolve task theo capability graph.

Example:

task: scrape website

resolve:

scrape → browser
browser → core/browser module


⸻

10. EXECUTION PLAN

Gemini phải tạo execution plan.

Example:

PLAN

1 validate task
2 resolve module
3 prepare runtime
4 execute module
5 validate output
6 store result

Plan lưu tại:

execution_plan.json


⸻

11. EXECUTION ENGINE

Gemini không thực thi trực tiếp.

Execution được chuyển tới:

factory_worker

Example call:

factory_worker.execute(plan)


⸻

12. RUNTIME LOGGING

Mọi execution phải ghi log.

Log locations:

logs/orchestrator.log
factory/logs/

Log format:

timestamp
task_id
module
result
status


⸻

13. VALIDATION

Sau khi execution:

Gemini phải chạy validation.

Sources:

tests/
verification scripts

Example:

tests/test_final_logic.py


⸻

14. RESULT STORAGE

Kết quả task được lưu tại:

factory/processed/

hoặc

reports/


⸻

15. CONTINUOUS SYSTEM AWARENESS

Gemini phải scan lại hệ thống định kỳ.

Interval:

5 minutes

Purpose:

detect new modules
detect code changes
update capability graph


⸻

16. SAFETY GUARDS

Gemini phải tuân thủ:

never modify source during scan
never execute unknown module
never bypass orchestrator
fail closed if dependency missing


⸻

17. MAIN LOOP

Pseudo runtime loop:

scan_filesystem()

catalog = classify_files()

index = semantic_read(catalog)

graph = build_capability_graph(index)

while True:

    task = check_inbox()

    if task:

        module = resolve_module(task)

        plan = build_plan(task,module)

        result = execute(plan)

        validate(result)

        log(result)


⸻

18. GEMINI ROLE

Gemini không phải execution worker.

Gemini là:

system interpreter
planner
dispatcher
validator

Worker thực thi là:

factory modules
system tools
runtime scripts


⸻

19. SYSTEM GOAL

Protocol này cho phép Gemini:

scan toàn bộ hệ
hiểu module
tự lập kế hoạch
điều phối thực thi

Gemini trở thành AI orchestrator của toàn bộ hệ thống.
