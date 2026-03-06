import subprocess
import json
import base64
import os
import sys

# --- SYNPATIC CONFIGURATION ---
USER_TARGET = "NguyenCuong1989"
KERNEL_PATH = "src/logic/kernel.py"
POOL_PATH = "src/logic/shared_pool.py"
SHARED_DIR = "shared_logic"
LIMIT = 100

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result

def synaptic_orchestration():
    print(f"Σ_APΩ: Initiating Cluster Synaptic Synchronization for {USER_TARGET}")
    
    if not os.path.exists(SHARED_DIR):
        os.makedirs(SHARED_DIR)

    # 1. Fetch Repository List
    print(f"Σ_APΩ: Retriving up to {LIMIT} repositories...")
    repo_list_cmd = f'gh repo list {USER_TARGET} --limit {LIMIT} --json name -q ".[].name"'
    repo_res = run_cmd(repo_list_cmd)
    
    if repo_res.returncode != 0:
        print(f"FAILED to retrieve repositories: {repo_res.stderr}")
        return

    repos = repo_res.stdout.strip().split("\n")
    print(f"Σ_APΩ: Found {len(repos)} repositories to analyze.")

    for repo in repos:
        if not repo: continue
        
        print(f"--- Processing: {repo} ---")
        
        # 2. Extract Logic Kernel
        extract_cmd = f"gh api repos/{USER_TARGET}/{repo}/contents/{KERNEL_PATH}"
        extract_res = run_cmd(extract_cmd)
        
        if extract_res.returncode != 0:
            print(f"SKIP: {KERNEL_PATH} not found or inaccessible in {repo}")
            continue

        try:
            data = json.loads(extract_res.stdout)
            content_b64 = data.get("content", "")
            kernel_code = base64.b64decode(content_b64).decode('utf-8')
        except Exception as e:
            print(f"ERROR: Failed to decode content from {repo}: {e}")
            continue

        # 3. Validate Logic (Compilation Check)
        temp_file = "temp_synapse.py"
        with open(temp_file, "w") as f:
            f.write(kernel_code)

        compile_res = run_cmd(f"python3 -m py_compile {temp_file}")
        if compile_res.returncode != 0:
            print(f"INVALID logic in {repo}. Compilation failed.")
            continue

        print(f"VALID logic found in {repo}. Persisting to {SHARED_DIR}")
        
        # 4. Save to Shared Logic
        local_target = os.path.join(SHARED_DIR, f"{repo}_kernel.py")
        with open(local_target, "w") as f:
            f.write(kernel_code)

        # 5. Synaptic Update (Shared Pool)
        # Re-encode to ensure clean base64
        encoded_content = base64.b64encode(kernel_code.encode('utf-8')).decode('utf-8')
        
        update_cmd = [
            "gh", "api", f"repos/{USER_TARGET}/{repo}/contents/{POOL_PATH}",
            "-X", "PUT",
            "-f", "message=logic: Synaptic Update from Cluster",
            "-f", f"content={encoded_content}"
        ]
        
        # Need to handle 'sha' for existing files (PUT requires SHA if file exists)
        check_pool_cmd = f"gh api repos/{USER_TARGET}/{repo}/contents/{POOL_PATH}"
        pool_res = run_cmd(check_pool_cmd)
        if pool_res.returncode == 0:
            pool_data = json.loads(pool_res.stdout)
            sha = pool_data.get("sha")
            update_cmd.extend(["-f", f"sha={sha}"])

        update_res = subprocess.run(update_cmd, capture_output=True, text=True)
        
        if update_res.returncode == 0:
            print(f"SUCCESS: Synaptic broadcast to {repo}/{POOL_PATH} complete.")
        else:
            print(f"FAILED to update {repo}/{POOL_PATH}: {update_res.stderr}")

    # Cleanup
    if os.path.exists("temp_synapse.py"):
        os.remove("temp_synapse.py")

if __name__ == "__main__":
    # Check if gh is authenticated
    auth_check = run_cmd("gh auth status")
    if auth_check.returncode != 0:
        print("CRITICAL: GitHub CLI not authenticated. Synchronization aborted.")
        sys.exit(1)
        
    synaptic_orchestration()
