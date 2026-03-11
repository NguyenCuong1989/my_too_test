# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import os
import time
from github import Github

def bulk_close_bot_issues():
    token = os.getenv('GITHUB_TOKEN')
    repo_name = 'NguyenCuong1989/DAIOF-Framework'

    if not token:
        print("Error: GITHUB_TOKEN not set")
        return

    g = Github(token)
    repo = g.get_repo(repo_name)

    # Target: Open issues created by the bot
    issues = repo.get_issues(state='open', creator='github-actions[bot]')

    count = 0
    for issue in issues:
        print(f"Closing recursive issue #{issue.number}: {issue.title}")
        issue.edit(state='closed', state_reason='not_planned')
        issue.create_comment("🔒 **Mesh Intervention**: This issue was identified as part of an automated recursion loop and has been closed to stabilize the repository. Ref: 4287.")
        count += 1
        if count >= 150: # Cap at 150 per run
            break
        time.sleep(1) # Avoid rate limits

    print(f"✅ Successfully closed {count} bot-generated issues.")

if __name__ == "__main__":
    bulk_close_bot_issues()
