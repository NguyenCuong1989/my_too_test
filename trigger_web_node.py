# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import asyncio
import logging
import sys
from autonomous_operator.nodes.web_node import WebNode

async def main():
    logging.basicConfig(level=logging.INFO)
    node = WebNode()
    try:
        print("🚀 Manually triggering WebNode...")
        await node.run_cycle()
        print("✅ WebNode finished successfully!")
    except Exception as e:
        print(f"❌ WebNode failed with: {e}")

if __name__ == "__main__":
    asyncio.run(main())
