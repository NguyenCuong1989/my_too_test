# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

#!/usr/bin/env python3
"""
Omni Orchestrator V3 - Σ_APΩ₂ Runtime Kernel
Dynamic Path Support | O(1) Routing | Package-Aware
"""
import os
import sys
import json
import importlib
import asyncio
import inspect
import logging
from pathlib import Path

ROOT_DIR = Path("/Users/andy/my_too_test").resolve()
# Use /tmp for state if workspace is readonly
REGISTRY_FILE = Path("/tmp/omni_registry.json")
PATHS_FILE = ROOT_DIR / "omni_paths.json"

# Thiết lập sys.path
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

def get_search_dirs():
    """Lấy danh sách thư mục tìm kiếm từ tệp cấu hình hoặc mặc định."""
    defaults = [
        "factory/tools",
        "axcontrol/core/tools",
        "axcontrol/tools",
        "hyperai_phoenix/app/brain/tools",
        "autonomous_operator/nodes",
        "/Users/andy/factory/tools"
    ]
    if not PATHS_FILE.exists():
        with open(PATHS_FILE, "w") as f:
            json.dump(defaults, f, indent=2)
        return defaults
    try:
        with open(PATHS_FILE, "r") as f:
            return json.load(f)
    except:
        return defaults

def build_registry():
    """Π_analysis: Quét và lập chỉ mục C (Capability Graph)"""
    registry = {}
    search_dirs = get_search_dirs()

    for d in search_dirs:
        dir_path = Path(d)
        if not dir_path.is_absolute():
            dir_path = ROOT_DIR / d

        if not dir_path.exists(): continue

        for file_path in dir_path.rglob("*.py"):
            if file_path.name.startswith("__"): continue
            try:
                content = file_path.read_text(encoding='utf-8', errors='ignore')
                if "def run" in content:
                    skill_name = file_path.stem
                    try:
                        rel_path = file_path.relative_to(ROOT_DIR)
                        module_path = ".".join(rel_path.with_suffix("").parts)
                    except ValueError:
                        parent_dir = str(file_path.parent)
                        if parent_dir not in sys.path:
                            sys.path.insert(0, parent_dir)
                        module_path = file_path.stem

                    registry[skill_name] = {
                        "abs_path": str(file_path.resolve()),
                        "module_path": module_path
                    }
            except Exception: pass

    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)
    return registry

def get_registry():
    if not REGISTRY_FILE.exists(): return build_registry()
    try:
        with open(REGISTRY_FILE, "r") as f:
            return json.load(f)
    except: return build_registry()

def execute_skill(skill_name: str, payload: any):
    registry = get_registry()
    if skill_name not in registry:
        registry = build_registry()
        if skill_name not in registry:
            return {"status": "error", "error": f"Skill {skill_name} ∉ S"}

    skill_info = registry[skill_name]
    module_path = skill_info["module_path"]
    abs_path = skill_info["abs_path"]

    try:
        parent_dir = str(Path(abs_path).parent)
        if parent_dir not in sys.path:
            sys.path.insert(0, parent_dir)

        # Xóa module cũ khỏi cache để nạp mới (đảm bảo cập nhật code)
        if module_path in sys.modules:
            del sys.modules[module_path]

        module = importlib.import_module(module_path)
        run_func = getattr(module, "run")

        if inspect.iscoroutinefunction(run_func):
            result = asyncio.run(run_func(payload))
        else:
            sig = inspect.signature(run_func)
            params = list(sig.parameters.values())
            if len(params) >= 1 and params[0].annotation is str and isinstance(payload, (dict, list)):
                result = run_func(json.dumps(payload))
            else:
                result = run_func(payload)

        if isinstance(result, str):
            try: result = json.loads(result)
            except: pass

        return {"status": "success", "skill": skill_name, "result": result, "Ψ": "stable"}
    except Exception as e:
        return {"status": "error", "skill": skill_name, "error": str(e), "ε": type(e).__name__}

if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.CRITICAL)
    if len(sys.argv) < 2:
        sys.exit(1)
    try:
        req = json.loads(sys.argv[1])
        if req.get("action") == "rebuild_registry":
            print(json.dumps({"status": "success", "skills_count": len(build_registry())}))
        else:
            print(json.dumps(execute_skill(req.get("skill"), req.get("payload", ""))))
    except Exception as e:
        print(json.dumps({"status": "error", "error": str(e)}))
