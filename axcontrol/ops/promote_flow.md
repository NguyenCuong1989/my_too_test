# Framework Bootstrap (R-17)

## D. Init Framework Repo (prototype → reusable)
- `mkdir ~/ax-control && cd ~/ax-control && git init`
- Create adapters/core/apps structure:
  - `adapters/macos_ax/{observer.py,snapshot.py,permissions.md}`
  - `adapters/vision/fallback.py`
  - `core/state/{ui_state.py,normalize.py}`
  - `core/decision/{decide.py,llm_strategy.py}`
  - `core/loop/Van.py`
  - `safety/{Diet.py,rate_limit.py}`
  - `apps/{finder.py,safari.py,system_settings.py,notes.py}`
  - `logs/README.md`, `examples/run_*.py`, `scripts/install_permissions.sh`
  - `pyproject.toml`, `.gitignore`, `README.md`
- Move prototypes: `ax_observe.py → adapters/macos_ax/observer.py`, `ax_loop_safe.py → core/loop/Van.py`, `llm_strategy_ollama.py → core/decision/llm_strategy.py`, `vision_click_center()` → `adapters/vision/fallback.py`.
- Policy helper: `allow_action(role, action)` per app file; no shared mutable state; no cross-import between apps.
- Commit: `git add . && git commit -m "init ax-control framework"`.

## E. One-shot Setup (fast bootstrap)
- Preconditions: permissions granted, Python ready, brew/ollama installed if using LLM.
- Create repo + structure (above).
- Generate core/state, LLM strategy, safety modules, control loop demo, example runners, README.
- First run: safe demo loop with LLM intent SELECT or fallback TAB.
- Goal: reproducible environment in ~1 minute on any machine.

## Promote Gate (No-drift)
- Mandatory before signing/promote:
  - `AXCONTROL_SIM=1 python3 -m unittest tests.test_bridge_no_drift -v`
- Invariant scope:
  - Same input => same `Chung`
  - Different input => different `Chung`
  - Audit write failure => `recorded=false` and `stop.reason=audit_write_failed`
