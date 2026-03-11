# \u03a3_AP\u03a9\u2082 CORE MODULE
# Authority: B\u1ed0 C\u01af\u1ed0NG Supreme System Commander
# Creator: alpha_prime_omega (4287)
# Status: CANONICAL

import asyncio
import json
import unittest
import sys
import os
from unittest.mock import MagicMock, patch

# Ensure the operator module can be loaded
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from orchestrator_v3 import AutonomousOperator

class TestPhase17NotionSync(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        # Mocking external components
        patcher_notion = patch('orchestrator_v3.Client')
        self.mock_notion = patcher_notion.start()
        self.addCleanup(patcher_notion.stop)

        patcher_link = patch('orchestrator_v3.NeuralLink')
        self.mock_link = patcher_link.start()
        self.addCleanup(patcher_link.stop)

        # Initialize Operator
        self.operator = AutonomousOperator()

        # Force inject mock notion components
        self.operator.notion = MagicMock()
        self.operator.notion_db_id = "test_db_id"
        self.operator.link = MagicMock() # Mock the link to avoid real DB hits

    async def test_coordinated_execution_with_args(self):
        # 1. Mock a Notion Command for WebScout with arguments
        mock_task = {
            'id': 'test_page_id',
            'properties': {
                'Command Name': {'title': [{'plain_text': 'Scout Google'}]},
                'Target': {'select': {'name': 'WebScout'}},
                'Arguments': {'rich_text': [{'plain_text': '{"url": "https://google.com"}'}]}
            }
        }

        # Configure Mock Notion query response
        self.operator.notion.databases.query.return_value = {'results': [mock_task]}

        # Mock WebNode run_cycle
        self.operator.web.run_cycle = MagicMock()

        # 2. Run pollination
        print(f"DEBUG: notion_db_id={self.operator.notion_db_id}")
        await self.operator.poll_notion_commands()

        # 3. Assertions
        # - Did the node receive the correct args?
        self.operator.web.run_cycle.assert_called_once_with(command_args='{"url": "https://google.com"}')

        # - Was the audit log created?
        self.operator.link.log_service_event.assert_any_call(
            service="Orchestrator",
            e_type="COMMAND_EXEC",
            content="Executed Scout Google on WebScout with args: {\"url\": \"https://google.com\"}",
            meta=unittest.mock.ANY
        )

        # - Was the Notion status updated to 'Complete'?
        self.operator.notion.pages.update.assert_called_once()
        args, kwargs = self.operator.notion.pages.update.call_args
        self.assertEqual(kwargs['properties']['Status']['select']['name'], 'Complete')

if __name__ == '__main__':
    unittest.main()
