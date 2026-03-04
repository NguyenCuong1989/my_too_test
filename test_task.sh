#!/bin/bash
# Test: Submit a task to the inbox

mkdir -p factory/inbox

cat > factory/inbox/test_enrichment_$(date +%s).task << 'TASK'
{
  "skill_name": "sli_enrichment",
  "task_id": "demo-enrichment-001",
  "parameters": {
    "company_name": "Tesla",
    "industry": "Electric Vehicles",
    "geo": "US"
  }
}
TASK

echo "✅ Task submitted to inbox. Check factory/processed/ in 5 seconds..."
sleep 5
echo "Processed tasks:"
ls -la factory/processed/ 2>/dev/null || echo "No processed tasks yet"
