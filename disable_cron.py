# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import os
import glob

workflow_dir = "/Users/andy/my_too_test/DAIOF-Framework/.github/workflows"
for filepath in glob.glob(os.path.join(workflow_dir, "*.yml")):
    with open(filepath, 'r') as f:
        content = f.read()

    new_lines = []
    # Simple hack to comment out schedule triggers
    for line in content.split('\n'):
        if ('schedule:' in line or 'cron:' in line) and not line.strip().startswith('#'):
            new_lines.append('# ' + line)
        else:
            new_lines.append(line)

    with open(filepath, 'w') as f:
        f.write('\n'.join(new_lines))

print("Disabled all cron schedules in github workflows.")
