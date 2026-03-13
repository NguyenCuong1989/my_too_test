import json
import subprocess
import os
import sys

def run_test():
    registry_path = '/Users/andy/my_too_test/omni_registry.json'
    if not os.path.exists(registry_path):
        print("❌ Cannot find omni_registry.json")
        sys.exit(1)

    with open(registry_path, 'r') as f:
        registry = json.load(f)

    print(f"🔍 BẮT ĐẦU PIPELINE KIỂM THỬ TOÀN DIỆN {len(registry)} MODULES")
    print("="*80)

    success = 0
    failed = 0
    results = []

    env = os.environ.copy()
    env["PYTHONPATH"] = f"/Users/andy/my_too_test:{env.get('PYTHONPATH', '')}"

    for skill, info in registry.items():
        # print(f"⏳ Đang kiểm thử [{skill}]...")
        cmd = ["/Users/andy/my_too_test/omni", skill, "{}"]
        try:
            out = subprocess.run(cmd, capture_output=True, text=True, timeout=45, env=env)

            # Phân tích cẩn thận stdout
            # Module được tính là lỗi nếu returncode != 0, hoặc có dòng báo "status": "error"
            # Thỉnh thoảng lỗi nằm trong stdout dưới dạng JSON.
            is_error = False
            error_details = ""

            if out.returncode != 0:
                is_error = True
                error_details = out.stderr.strip() or out.stdout.strip()
            elif "error" in out.stdout.lower() and "success" not in out.stdout.lower():
                is_error = True
                error_details = out.stdout.strip()
            elif "modulenotfounderror" in out.stdout.lower() or "exception" in out.stdout.lower() and "success" not in out.stdout.lower():
                is_error = True
                error_details = out.stdout.strip()

            if not is_error:
                print(f"   ✅ [PASSED] {skill}")
                success += 1
                results.append((skill, "PASSED", out.stdout.strip()))
            else:
                print(f"   ❌ [FAILED] {skill}")
                failed += 1
                short_err = error_details[:200].replace('\n', ' ') + "..." if len(error_details) > 200 else error_details.replace('\n', ' ')
                results.append((skill, "FAILED", short_err))

        except subprocess.TimeoutExpired:
            print(f"   ⚠️ [TIMEOUT] {skill}")
            failed += 1
            results.append((skill, "TIMEOUT", "Hết thời gian chờ (15s)"))
        except Exception as e:
            print(f"   ❗️ [CRITICAL] {skill}: {str(e)}")
            failed += 1
            results.append((skill, "CRITICAL", str(e)))

    print("\n" + "="*80)
    print(f"📊 BÁO CÁO PIPELINE: HOÀN THÀNH {success}/{len(registry)} MODULES (FAILED/TIMEOUT: {failed})")
    print("="*80)

    with open('/Users/andy/my_too_test/module_audit_report.md', 'w') as f:
        f.write(f"# Báo cáo Pipeline Kiểm thử Modules (APΩ)\n\n")
        f.write(f"**Tổng số modules:** {len(registry)}\n")
        f.write(f"**Passed:** {success}\n")
        f.write(f"**Failed:** {failed}\n\n")
        f.write("## Chi tiết:\n\n")
        f.write("| Module (Skill) | Trạng thái | Ghi chú / Lỗi |\n")
        f.write("| --- | --- | --- |\n")
        for r in results:
            status_icon = "🟢" if r[1] == "PASSED" else "🔴" if r[1] == "FAILED" else "⚠️"
            note = r[2].replace('|', '&#124;').replace('\n', ' ')[:100] + "..." if len(r[2]) > 100 else r[2].replace('|', '&#124;').replace('\n', ' ')
            f.write(f"| {r[0]} | {status_icon} {r[1]} | `{note}` |\n")

if __name__ == '__main__':
    run_test()
