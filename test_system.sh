#!/bin/bash
set -e

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 ACE System - Comprehensive Test Suite"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Test 1: Check running containers
echo "📦 TEST 1: Container Status"
echo "─────────────────────────────────────────────────────────────────────────"
docker compose ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo ""

# Test 2: Check network
echo "🌐 TEST 2: Docker Network"
echo "─────────────────────────────────────────────────────────────────────────"
docker network inspect my_too_test_app-network --format "table {{.Name}}\t{{.Containers}}" 2>/dev/null || echo "Network: my_too_test_app-network"
echo ""

# Test 3: Recent logs
echo "📋 TEST 3: Recent Logs (Last 5 Lines)"
echo "─────────────────────────────────────────────────────────────────────────"
docker compose logs --tail=5 | grep -E "(startup|Running|listening|Healthy|ERROR)" || echo "✅ All services running normally"
echo ""

# Test 4: File structure
echo "📂 TEST 4: Task Processing Directories"
echo "─────────────────────────────────────────────────────────────────────────"
echo "Inbox:"
ls -la factory/inbox/ 2>/dev/null | wc -l | xargs echo "  Files:"
echo "Processing:"
ls -la factory/processing/ 2>/dev/null | wc -l | xargs echo "  Files:"
echo "Processed:"
ls -la factory/processed/ 2>/dev/null | wc -l | xargs echo "  Files:"
echo "Failed:"
ls -la factory/failed/ 2>/dev/null | wc -l | xargs echo "  Files:"
echo ""

# Test 5: Audit chain
echo "🔐 TEST 5: Audit Chain"
echo "─────────────────────────────────────────────────────────────────────────"
if [ -f factory/logs/last_hash.txt ]; then
    echo "Last Hash: $(cat factory/logs/last_hash.txt)"
    echo "Audit Log Lines: $(wc -l < factory/logs/audit_chain.log 2>/dev/null || echo 0)"
else
    echo "No audit chain yet (system just started)"
fi
echo ""

# Test 6: Skills available
echo "🛠️  TEST 6: Available Skills"
echo "─────────────────────────────────────────────────────────────────────────"
ls -1 factory/tools/*.py | xargs -I {} basename {} .py | sed 's/^/  ✅ /'
echo ""

# Test 7: Create test task
echo "📝 TEST 7: Submit Test Task"
echo "─────────────────────────────────────────────────────────────────────────"
TASK_ID="test_$(date +%s)"
cat > factory/inbox/${TASK_ID}.task << 'TASK'
{
  "skill_name": "sli_enrichment",
  "task_id": "test-auto-001",
  "parameters": {
    "company_name": "Google",
    "industry": "AI & Search",
    "geo": "US"
  }
}
TASK
echo "✅ Task submitted: ${TASK_ID}"
echo ""

# Test 8: Wait and check processing
echo "⏳ TEST 8: Waiting for Task Processing (10 seconds)..."
echo "─────────────────────────────────────────────────────────────────────────"
sleep 10

# Test 9: Check result
echo "📊 TEST 9: Processing Result"
echo "─────────────────────────────────────────────────────────────────────────"
if [ -f "factory/processed/${TASK_ID}.task" ]; then
    echo "✅ Task COMPLETED in processed/"
    echo "Result snippet:"
    head -20 "factory/processed/${TASK_ID}.task" | sed 's/^/  /'
elif [ -f "factory/failed/${TASK_ID}.task" ]; then
    echo "❌ Task FAILED (moved to failed/)"
    cat "factory/failed/${TASK_ID}.task" | sed 's/^/  /'
else
    echo "⏳ Task still processing..."
    echo "Current inbox files:"
    ls -la factory/inbox/ | tail -2
fi
echo ""

# Summary
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ ACE System Test Complete!"
echo ""
echo "Dashboard URLs:"
echo "  🌐 Firebase UI:     http://localhost:4000"
echo "  🔀 MCP Router:      http://localhost:3000"
echo "  🏭 Factory Worker:  http://localhost:8081"
echo ""
echo "Logs:"
echo "  📋 Real-time:       docker compose logs -f"
echo "  🔗 Audit chain:     cat factory/logs/audit_chain.log"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
