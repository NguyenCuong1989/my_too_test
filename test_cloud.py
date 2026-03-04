import sys
import os
import logging

# Ensure we can import autonomous_operator
sys.path.append('/Users/andy/my_too_test')

from autonomous_operator.nodes.biz_node import BizNode

# Configure logging to console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(name)s] [%(levelname)s] %(message)s',
    stream=sys.stdout
)

def test_cloud_delegation():
    print("🚀 STARTING REAL-TIME POC: BIZNODE CLOUD DELEGATION")

    # Mock config
    config = {
        'NOTION_DB_ID': 'test_db',
        'SCOPES': []
    }

    # Initialize BizNode
    biz = BizNode(config)

    # Test Case: Heavy Task (Long snippet)
    print("\n--- CASE 1: HEAVY TASK (EXPECT CLOUD DELEGATION) ---")
    heavy_snippet = "This is a very long text to trigger cloud delegation logic. " * 30
    subject = "Complex System Audit"

    print(f"Snippet length: {len(heavy_snippet)}")

    try:
        # This will call delegate_task -> delegate_to_cloud_cli
        # It will use 'gh copilot explain' by default for github hub
        print("⚡ Executing analyze_ai with use_cloud=True...")
        result = biz.analyze_ai(subject, heavy_snippet, use_cloud=True)
        print(f"✅ Result from Cloud Worker:\n{result}")
    except Exception as e:
        print(f"❌ Delegation Error (Expected if not logged into gh): {str(e)}")

if __name__ == "__main__":
    test_cloud_delegation()
