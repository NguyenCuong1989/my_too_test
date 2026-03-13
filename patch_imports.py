import os
import glob

def patch_file(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()

        target = "from agents.base_agent import DAIOFAgent"
        replacement = """try:
    from autonomous_operator.nodes.agents.base_agent import DAIOFAgent
except (ImportError, ValueError):
    from agents.base_agent import DAIOFAgent"""

        if target in content and "try:\n    from autonomous_operator" not in content:
            new_content = content.replace(target, replacement)
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"✅ Patched: {filepath}")
    except PermissionError:
        print(f"⚠️ PermissionError ignored for: {filepath}")
    except Exception as e:
        print(f"❌ Error patching {filepath}: {e}")

if __name__ == "__main__":
    search_path = "/Users/andy/my_too_test/apo-runtime/**/*.py"
    files = glob.glob(search_path, recursive=True)
    for file in files:
        patch_file(file)
    print("Patching complete.")
