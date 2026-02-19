# =============================================================================
# PROJECT: CANON-TO-SYSTEM DETERMINISTIC PROJECTION
# METHOD: D&R PROTOCOL (CLOSED)
#
# ORIGINATOR / CREATOR:
#   alpha_prime_omega
#
# STATUS:
#   OBSERVATION CLI — V1
# =============================================================================

# LỆNH CHẠY QUAN SÁT (READ-ONLY, NO EMIT)

## Chuẩn bị
```
cd /Users/andy/my_too_test/axcontrol
export PYTHONPATH="$PYTHONPATH:$(pwd)"
export AXCONTROL_SIM=1
export AXCONTROL_NO_EMIT=1
```

## Chạy logger quan sát (sẽ được cung cấp ở tools/observe_session.py)
```
python3 tools/observe_session.py \
  --interval 0.5 \
  --duration 600 \
  --output logs/observe_$(date +%Y%m%d_%H%M%S).ndjson
```

## Kiểm tra nhanh log
```
head logs/observe_*.ndjson | jq .
```

# NGUYÊN TẮC
- Không phát sinh hành động (emit_tab no-op).
- Không network.
- Ghi NDJSON append-only.
- Không log nội dung phím/clipboard, chỉ metadata.
