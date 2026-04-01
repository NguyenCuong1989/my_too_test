# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import json
import os
import subprocess

with open('/Users/andy/my_too_test/daiof_issues.json', 'r') as f:
    issues = json.load(f)

# Find issues to close
to_close = []
for issue in issues:
    title = issue['title']
    if "EMERGENCY" in title or "CI/CD Failure" in title:
        to_close.append(issue['number'])

if to_close:
    print(f"Closing {len(to_close)} issues...")
    # run gh issue close
    for i in range(0, len(to_close), 20):
        chunk = to_close[i:i+20]
        cmd = ["gh", "issue", "close", "-R", "NguyenCuong1989/DAIOF-Framework"] + [str(num) for num in chunk]
        subprocess.run(cmd)
    print("Issues closed!")
else:
    print("No spam issues found.")
