# =============================================================================
# PROJECT: CANON-TO-SYSTEM DETERMINISTIC PROJECTION
# METHOD: D&R PROTOCOL (CLOSED)
#
# ORIGINATOR / CREATOR:
#   alpha_prime_omega
#
# STATUS:
#   CANONICAL SCHEMA — OBS-PHASE-V1
# =============================================================================

# I. ĐỊNH NGHĨA TRƯỜNG DỮ LIỆU CỐ ĐỊNH (FIELD DEFINITIONS)

| Field  | Type   | Description                                                      |
| :----- | :----- | :--------------------------------------------------------------- |
| `type` | string | Phân loại record: input, ax, system, human_state, llm.          |
| `ts`   | float  | Unix timestamp (precision: 0.001s).                              |
| `sub`  | string | Phân loại phụ (key, mouse, copy, paste, start, end).             |
| `app`  | string | Bundle Identifier của ứng dụng focus.                            |
| `role` | string | AXRole của phần tử UI.                                           |
| `hex`  | string | 6-bit Hexagram (state_projector output).                         |
| `state`| string | Phân loại Human: H0, H1, H2.                                     |
| `model`| string | ID của Model (Ollama/CLI).                                       |

# II. CẤU TRÚC RECORD (OBJECT SCHEMAS)

## 1. Type: `input`
{
  "ts": 1740000000.123,
  "type": "input",
  "sub": "key",
  "keycode": 48,
  "mod": ["cmd"]
}

## 2. Type: `ax`
{
  "ts": 1740000000.456,
  "type": "ax",
  "app": "com.apple.finder",
  "role": "AXWindow",
  "label": "Downloads",
  "hex": "010101"
}

## 3. Type: `human_state`
{
  "ts": 1740000001.000,
  "type": "human_state",
  "state": "H1"
}

## 4. Type: `llm`
{
  "ts": 1740000002.789,
  "type": "llm",
  "event": "start",
  "model": "deepseek-r1:8b"
}

# III. RÀNG BUỘC (CONSTRAINTS)

- File Format: NDJSON (Newlined Delimited JSON).
- Encoding: UTF-8.
- Write Mode: Append-only.
- Privacy: Tuyệt đối không lưu giá trị `key_string`, `clipboard_data`, hoặc `ax_value`.
