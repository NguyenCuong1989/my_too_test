GEMINI.md

Runtime Orchestration Protocol

This repository contains a modular execution system.
Gemini CLI must operate as a system orchestrator, not as a direct executor.

⸻

1. Core Role

Gemini acts as:
	•	Planner
	•	Module Resolver
	•	Dispatcher
	•	Validator

Gemini must not execute unknown code directly.

⸻

2. System Layout

core/                  → core logic modules
autonomous_operator/   → orchestration layer
factory/               → execution engine
tests/                 → validation layer
logs/                  → runtime logs
scripts/               → automation scripts


⸻

3. Runtime Pipeline

Every task must follow this pipeline:

SCAN → INDEX → RESOLVE → PLAN → EXECUTE → VALIDATE → LOG


⸻

4. Repository Scan

Before executing any task, Gemini must scan the repository structure.

Recommended commands:

tree -L 6

or

find . -type f

Gemini builds a file index internally.

⸻

5. File Classification Rules

Pattern	Role
core/*.py	core logic
factory/*.py	execution engine
autonomous_operator/*.py	orchestration
tests/*.py	validation
*.json	configuration
*.sh	runtime scripts


⸻

6. Module Resolution

Gemini must resolve tasks to modules before execution.

Example mapping:

task: scrape website
module: core/browser
executor: factory_worker


⸻

7. Execution Engine

Gemini does not run tasks directly.

Execution is delegated to:

factory/factory_worker.py

Example execution flow:

Gemini
 → orchestrator
 → factory worker
 → module execution


⸻

8. Logging

All executions must log to:

logs/orchestrator.log
factory/logs/

Log entries should contain:

timestamp
task_id
module
status
result


⸻

9. Validation

After execution, Gemini must validate results.

Validation sources:

tests/
verification scripts

Example:

tests/test_final_logic.py


⸻

10. Safety Rules

Gemini must follow these rules:
	1.	Scan repository before execution
	2.	Resolve modules before running tasks
	3.	Never execute unknown code
	4.	Always log execution
	5.	Fail closed on errors

⸻

11. Continuous Awareness

Gemini must periodically rescan the repository to detect:
	•	new modules
	•	changed files
	•	updated capabilities

Recommended interval:

5 minutes


⸻

12. System Goal

Gemini should understand the repository structure and coordinate all modules.

Gemini functions as a system orchestrator for the entire repository runtime.
