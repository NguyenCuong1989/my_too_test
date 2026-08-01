#!/usr/bin/env bash
# end-to-end smoke test — every assertion exits non-zero on failure
set -euo pipefail

BASE="${BASE:-http://localhost:3000}"
echo "═══ Σ_APΩ-COS SMOKE TEST — target $BASE ═══"

j() { python3 -c "import sys,json; print(json.dumps(json.loads(sys.stdin.read()), indent=2))"; }

echo
echo "[1] mcp-router health"
H=$(curl -sS "$BASE/health")
echo "$H" | j
python3 -c "import sys,json; d=json.loads(sys.stdin.read()); sys.exit(0 if d.get('ok') else 1)" <<< "$H" || { echo "FAIL: router not healthy"; exit 1; }

echo
echo "[2] mint token (subject=mcp-router)"
T=$(curl -sS -X POST "$BASE/auth/token" -H "Content-Type: application/json" \
    -d '{"subject":"smoke-test","constraints":{"max_objects":50,"max_arrays":25,"max_depth":8}}' \
    | python3 -c "import sys,json; print(json.loads(sys.stdin.read())['token'])")
echo "token = ${T:0:40}..."

echo
echo "[3] call factory-worker via mcp-router"
R=$(curl -sS -X POST "$BASE/call/factory-worker" \
    -H "Authorization: Bearer $T" -H "Content-Type: application/json" \
    -d '{"method":"POST","path":"/process","body":{"task":"hello","payload":{"a":1,"b":[1,2,3]}}}')
echo "$R" | j
echo "$R" | grep -q '"sigma"' || { echo "FAIL: factory-worker did not return sigma state"; exit 1; }

echo
echo "[4] call ai-sidecar directly (port 8100)"
A=$(curl -sS -X POST http://localhost:8100/process \
    -H "Authorization: Bearer $T" -H "Content-Type: application/json" \
    -d '{"prompt":"hi","payload":{"x":{"y":[1,2]}}}')
echo "$A" | j
echo "$A" | grep -q '"echo"' || { echo "FAIL: ai-sidecar offline mode broken"; exit 1; }

echo
echo "[5] mcp-router → factory-worker → relay → ai-sidecar (chain)"
R=$(curl -sS -X POST "$BASE/call/factory-worker" \
    -H "Authorization: Bearer $T" -H "Content-Type: application/json" \
    -d '{"method":"POST","path":"/process","body":{"task":"chain","payload":{"nested":{"a":1}},"forward_to":"ai-sidecar"}}')
echo "$R" | j
echo "$R" | grep -q 'forwarded_to' || { echo "FAIL: chain relay did not forward"; exit 1; }
echo "$R" | grep -q 'forward_result' || { echo "FAIL: no forward_result returned"; exit 1; }

echo
echo "[6] connector Asana (no token → expect 503 configured-but-empty)"
C=$(curl -sS -o /dev/null -w "%{http_code}" -X POST "$BASE/connector/asana" \
    -H "Authorization: Bearer $T" -H "Content-Type: application/json" \
    -d '{"path":"/users/me","method":"GET"}')
echo "  status=$C (expect 503 because ASANA_PAT not set)"
test "$C" = "503" || { echo "FAIL: connector should return 503 when env var empty"; exit 1; }

echo
echo "[7] health of all internal services"
H=$(curl -sS "$BASE/health/all")
echo "$H" | j
echo "$H" | grep -q '"factory-worker"' || { echo "FAIL: health/all missing factory-worker"; exit 1; }
echo "$H" | grep -q '"ai-sidecar"'     || { echo "FAIL: health/all missing ai-sidecar"; exit 1; }

echo
echo "═══ ALL SMOKE TESTS PASSED ═══"