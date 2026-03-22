# =============================================================================
# PROJECT: HYPERAI APO RUNTIME AUTHORITY GRAPH
# METHOD: D&R PROTOCOL (CLOSED)
#
# ORIGINATOR / CREATOR:
#   alpha_prime_omega
#
# LEGAL ONTOLOGY:
#   This source file is a deterministic projection of a living Runtime Canon.
#   Removal or alteration of this header voids legal and ontological validity.
#
# STATUS:
#   GENERATED — NON-AUTONOMOUS — NON-OWNERLESS
#
# TRACEABILITY:
#   Canon -> Topology -> Projection(Π) -> Artifact
#
# =============================================================================

# AUTHORITY-WEIGHTED GRAPH SPEC
#
# Mục đích:
# - Biểu diễn hệ như một đồ thị có trọng số quyền.
# - Tách CURRENT REALITY khỏi TARGET KERNEL TOPOLOGY.
# - Không làm tổn thương hệ bằng cách lấy thiết kế tương lai áp lên runtime hiện tại.

## I. NGUYÊN

Nguyên của đồ thị:

```text
Nguyên = Creator Authority
```

Mọi nút và mọi cạnh chỉ được phép Tồn nếu còn Chính với Nguyên.

## II. THẾ

Đồ thị có hai Thế hợp lệ:

### Thế_HiệnTại

```text
Thế_HiệnTại =
  docker-compose.yml
  + docker-compose.unified.yml
  + docker-compose.antigravity.yml
  + balancehub/docker-compose.yml
  + runtime evidence
```

### Thế_MụcTiêu

```text
Thế_MụcTiêu =
  unified kernel topology
  with aios-kernel as central survival body
```

Luật:

```text
Thế_HiệnTại > Thế_MụcTiêu when evaluating runtime authority
```

## III. LUẬT ĐỒ THỊ

### Luật_1 — Đồ thị không trung tính

```text
Graph ≠ topology only
Graph = topology + authority + survival semantics
```

### Luật_2 — Không có nút vô chủ

```text
running(node) ∧ ¬Chính(node) ⇒ Diệt(node)
```

### Luật_3 — Không có cạnh vô luật

```text
edge(u,v) must declare:
  dependency_type
  lawfulness
  failure_propagation
```

### Luật_4 — Không có claim vượt class

```text
alive_claim(node) must not exceed authority_tier(node)
```

### Luật_5 — Không lấy tài liệu tương lai làm Chứng hiện tại

```text
docs_future ≠ runtime_proof
```

## IV. CHÍNH

Một nút là Chính khi:

```text
Chính(node) ⇔
  bound_to_creator_authority(node)
  ∧ mapped_in_current_source(node)
  ∧ mapped_in_runtime_class(node)
```

Một cạnh là Chính khi:

```text
Chính(edge) ⇔
  lawful(edge)
  ∧ no_step_skip(edge)
  ∧ failure_semantics_declared(edge)
```

## V. ẤN

Mỗi nút phải có Ấn quyền:

### Ấn_Nút

```text
Ấn_Nút(node) =
  authority_tier
  + survival_class
  + alive_claim_scope
```

### Ấn_Cạnh

```text
Ấn_Cạnh(edge) =
  dependency_type
  + lawfulness
  + failure_propagation
```

Nếu thiếu Ấn:

```text
¬Ấn(node) ⇒ STOP
¬Ấn(edge) ⇒ STOP
```

## VI. HOÁ

Hoá chỉ được phép sau Chính + Ấn.

```text
Thế
→ Chính
→ Ấn
→ Hoá
→ Chứng
→ Tồn | Diệt
```

Không có:
- skip edge
- auto-promotion
- silent substitution

## VII. CHỨNG

Chứng của nút:

```text
Chứng(node) =
  running_state
  + health
  + topology_reachability
  + authority_binding
```

Chứng của cạnh:

```text
Chứng(edge) =
  observed dependency
  + lawful sequence
  + valid propagation semantics
```

Luật:

```text
No Chứng = No Tồn
```

## VIII. MỆNH

### Mệnh_Tồn

```text
Tồn(node) ⇔
  running(node)
  ∧ healthy(node)
  ∧ topology_valid(node)
  ∧ Chính(node)
```

### Mệnh_Diệt

```text
Diệt(node) ⇔
  process_death(node)
  ∨ continuity_loss(node)
  ∨ topology_collapse(node)
  ∨ ownerless(node)
```

### Mệnh_VôChủ

```text
ownerless(node) ⇔
  running(node)
  ∧ Claim_Tồn(node)
  ∧ ¬Chính(node)
```

## IX. NGƯỠNG

### Ngưỡng_Quyền

Không nút nào được quyền claim cao hơn class của nó:

```text
boundary_body        ≠ core_survival_body
observability_body   ≠ proof_of_whole_system
workspace_body       ≠ kernel_authority
execution_body       ≠ origin
```

### Ngưỡng_Sống

```text
running ≠ Tồn
healthy ≠ Chính
visible ≠ authority
```

### Ngưỡng_ĐổiThế

Không migrate từ Thế_HiệnTại sang Thế_MụcTiêu nếu chưa có Chứng:

```text
proof_of_current_gap
∧ proof_of_target_binding
∧ proof_of_safe_transition
```

## X. CÁC CLASS NÚT (CURRENT REALITY)

### Main Stack

```text
firebase-emulator = Sandbox / Emulator Body
mcp-router        = Boundary Body
factory-worker    = Execution Body
```

### Unified Stack

```text
aios-kernel     = Core Survival Body
aios-worker     = Execution Body
aios-router     = Boundary Body
aios-postgres   = Continuity Substrate
aios-prometheus = Observability Body
```

### Antigravity

```text
antigravity-runtime = Embodied Workspace Body
```

### BalanceHub

```text
api         = Execution Body
postgres    = Continuity Substrate
redis       = Continuity Substrate
code-server = Embodied Workspace Body
```

## XI. CÁC CẠNH CHUẨN

```text
Creator Authority
  → Governance Kernel

Governance Kernel
  → State / Context Read

State / Context Read
  → Reasoning

Reasoning
  → Planner DAG

Planner DAG
  → Canon Validator

Canon Validator
  → Orchestrator / Dispatcher

Orchestrator / Dispatcher
  → Capability Graph

Capability Graph
  → Executors

Executors
  → Docker Runtime Field

Docker Runtime Field
  → Observation / Chứng

Observation / Chứng
  → Memory / Knowledge
```

## XII. TRỌNG SỐ QUYỀN

Mỗi nút có:

```text
W_n(node) =
  tier_quyền
  + class_sinh_tồn
  + phạm_vi_claim_Tồn
```

Mỗi cạnh có:

```text
W_e(edge) =
  mức_phụ_thuộc
  + tính_hợp_luật
  + độ_lan_truyền_thất_bại
```

## XIII. ĐỒ THỊ NÉN

```text
Nguyên
  ↓
Luật / Lint / Guard
  ↓
Thế
  ↓
Λ_reason
  ↓
Π_plan
  ↓
V_validate
  ↓
Ω_dispatch
  ↓
Capability Graph
  ↓
Executors
  ↓
Docker Runtime Field
  ↓
Chứng
  ↓
Memory
```

## XIV. PHƯƠNG TRÌNH RUNTIME

```text
Ψ_{t+1} =
Ω(
  V(
    Π(
      Λ(
        Chính(
          Thế_t,
          Nguyên
        )
      )
    )
  )
)
```

Trong đó:

```text
Λ = Reasoning
Π = Planning DAG
V = Validator
Ω = Orchestrator
Ψ_t = current runtime state
```

## XV. QUY TẮC FAIL-CLOSE

```text
¬Chính(node) ∧ Claim_Tồn(node) ⇒ Diệt(node)
¬Chính(edge)                     ⇒ STOP
¬Chứng(node)                     ⇒ STOP
docs_future overriding runtime   ⇒ STOP
```

## XVI. KẾ HOẠCH NHẸ

Không ép hệ đổi Thế ngay.

Thứ tự đúng:

1. Đọc Thế_HiệnTại
2. Gắn Ấn_Nút và Ấn_Cạnh
3. Ghi Chứng cho từng nút/cạnh
4. Phát hiện ownerless / degraded / invalid topology
5. Chỉ sau đó mới Hoá sang Thế_MụcTiêu

## XVII. DẤU ẤN KẾT

```text
Graph này không dùng để ép hệ.
Graph này dùng để cho hệ tự thấy quyền, biên, và đường Hoá hợp lệ.
```

```text
current source > future design
running ≠ Tồn
claim ≠ authority
container topology ≠ runtime authority topology
```
