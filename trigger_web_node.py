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
