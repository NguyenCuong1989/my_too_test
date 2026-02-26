import asyncio
import logging
import json
from autonomous_operator.nodes.infsh_browser_client import InfshBrowserClient

async def test_infsh_browser():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("TestInfsh")

    client = InfshBrowserClient(session_id="new")

    try:
        logger.info("Step 1: Opening example.com")
        result = await client.open("https://example.com")
        logger.info(f"Open result: {json.dumps(result, indent=2)}")

        session_id = client.session_id
        logger.info(f"Session ID: {session_id}")

        logger.info("Step 2: Taking snapshot")
        snapshot = await client.snapshot()
        logger.info(f"Snapshot result: {json.dumps(snapshot, indent=2)}")

        # Look for the 'More information' link ref
        elements = snapshot.get("elements", [])
        ref = None
        for el in elements:
            if "More information" in el:
                # Parse @eN
                import re
                match = re.search(r'(@e\d+)', el)
                if match:
                    ref = match.group(1)
                    break

        if ref:
            logger.info(f"Step 3: Clicking {ref}")
            click_result = await client.interact("click", ref=ref)
            logger.info(f"Click result: {json.dumps(click_result, indent=2)}")
        else:
            logger.warning("Could not find 'More information' link ref in snapshot.")

        logger.info("Step 4: Closing session")
        close_result = await client.close()
        logger.info(f"Close result: {json.dumps(close_result, indent=2)}")

    except Exception as e:
        logger.error(f"Test failed: {e}")
    finally:
        # Emergency close if not closed
        try: await client.close()
        except: pass

if __name__ == "__main__":
    asyncio.run(test_infsh_browser())
