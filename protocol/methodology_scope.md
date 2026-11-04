# Methodological Scope — v0.2 (ADOPTED)

**Status:** Adopted, version 0.2, 2026-11-04.
**Basis:** RQ-D2 (Section 6.4 of the manuscript).
**Depends on:** All four foundational documents (all adopted, v0.2).

---

## 1. Purpose

This document determines the methodological scope of Research II. It answers RQ-D2: what methodological approaches are adequate for examining the questions in families A–C?

The determination follows the adoption of all four foundational documents (Conceptual Architecture, Authority Structure, Representation Lifecycle, Research Questions), as required by the program's sequential adoption discipline (Section 8.1).

---

## 2. Determination

**Methodology:** Mixed Methods, with **Document Analysis** as the primary approach and **Case Study** / **Comparative Analysis** as secondary approaches.

| Approach | Role | Families |
|---|---|---|
| **Document Analysis** | Primary | A, B |
| **Case Study** | Secondary | B, C |
| **Comparative Analysis** | Tertiary | A, B, C |

This is a **sequential mixed-methods design**: Document Analysis first, Case Study second, Comparative Analysis third.

---

## 3. Justification

### 3.1 Why Document Analysis First

Document Analysis is the least resource-intensive approach and the most directly aligned with the program's structural questions. It allows examination of:

- **Function assignment** (RQ-A1): which entities perform which functions, as stated in platform policies and transparency documents.
- **Authority distribution** (RQ-B1–B6): which entities claim which authorities, as stated in terms of service, content policies, and transparency reports.
- **Structural interruptions** (RQ-C3): which stages of the lifecycle are explicitly governed, as stated in policy documents.

Document Analysis does not require access to proprietary systems, user data, or APIs. It is reproducible, verifiable, and aligned with the program's commitment to structural analysis.

### 3.2 Why Case Study Second

Case Study allows deeper examination of a single system, including:

- **Lifecycle paths** (RQ-C1, RQ-C2): which paths a representation takes in a specific system.
- **Re-origination cycles** (RQ-C4): how reception returns to production in a specific system.
- **Recipient interpretive authority** (RQ-C5): how the recipient's interpretive position operates in a specific system.

Case Study is secondary because it requires more resources than Document Analysis and is less easily generalized.

### 3.3 Why Comparative Analysis Third

Comparative Analysis allows cross-system comparison, including:

- **Recurring authority patterns** (RQ-B6): which patterns recur across systems.
- **Function-authority alignment** (RQ-A3): which structural conditions determine whether functions and authorities coincide or diverge.

Comparative Analysis is tertiary because it depends on the findings of Document Analysis and Case Study.

---

## 4. Systems Selected for Analysis

### 4.1 Primary Systems (Document Analysis)

| System | Developer | Rationale |
|---|---|---|
| **ChatGPT** | OpenAI | Most widely used conversational AI; extensive policy documentation |
| **Gemini** | Google | Integrated with search and workspace; distinct distribution interface |
| **Claude** | Anthropic | Constitutional AI approach; distinct interpretive authority claims |
| **Perplexity** | Perplexity AI | Search-augmented generation; distinct selection and distribution functions |

**Selection criteria:**
1. Publicly available policy documentation.
2. Distinct architectural configurations (not all integrated platforms).
3. Sufficient user base to be structurally significant.

### 4.2 Secondary Systems (Case Study)

| System | Rationale |
|---|---|
| **ChatGPT** | Most documented; suitable for detailed lifecycle analysis |

### 4.3 Tertiary Systems (Comparative Analysis)

All primary systems, compared pairwise.

---

## 5. Data Sources

### 5.1 Document Analysis

| Source Type | Examples |
|---|---|
| **Terms of Service** | OpenAI ToS, Google ToS, Anthropic ToS |
| **Content Policies** | Usage policies, content moderation guidelines |
| **Transparency Reports** | OpenAI transparency reports, Google transparency reports |
| **Model Cards** | GPT-4 model card, Gemini model card, Claude model card |
| **Privacy Policies** | Data retention, access, and distribution policies |

### 5.2 Case Study

| Source Type | Examples |
|---|---|
| **API Documentation** | Request/response structures, rate limits, access controls |
| **Interface Analysis** | UI elements that determine presentation, ranking, filtering |
| **Public Statements** | Blog posts, technical reports, safety announcements |

### 5.3 Comparative Analysis

Findings from 5.1 and 5.2, compared across systems.

---

## 6. Implementation Phases

### Phase 1 — Document Analysis (Priority: First)

| Step | Task | Output |
|---|---|---|
| 1.1 | Collect policy documents for 4 systems | `DATA/raw/policies/` |
| 1.2 | Code documents for functions (5) | Function matrix |
| 1.3 | Code documents for authorities (5) | Authority matrix |
| 1.4 | Identify structural interruptions | Interruption log |
| 1.5 | Report findings | `REPORTS/phase_1_document_analysis.md` |

**Timeline:** 4–6 weeks.
**Deliverable:** Function matrix, authority matrix, interruption log.

### Phase 2 — Case Study (Priority: Second)

| Step | Task | Output |
|---|---|---|
| 2.1 | Select one system (ChatGPT) | Case selection note |
| 2.2 | Trace lifecycle paths | Lifecycle path log |
| 2.3 | Examine re-origination cycles | Re-origination log |
| 2.4 | Examine recipient interpretive authority | Interpretive position note |
| 2.5 | Report findings | `REPORTS/phase_2_case_study.md` |

**Timeline:** 3–4 weeks.
**Deliverable:** Lifecycle path log, re-origination log.

### Phase 3 — Comparative Analysis (Priority: Third)

| Step | Task | Output |
|---|---|---|
| 3.1 | Compare function matrices across systems | Comparative function matrix |
| 3.2 | Compare authority matrices across systems | Comparative authority matrix |
| 3.3 | Identify recurring patterns | Pattern log |
| 3.4 | Report findings | `REPORTS/phase_3_comparative_analysis.md` |

**Timeline:** 3–4 weeks.
**Deliverable:** Comparative matrices, pattern log.

---

## 7. Methodological Commitments

### 7.1 Structural, Not Normative

The methodology examines how functions and authorities are **distributed**, not whether the distribution is **just** or **efficient**. Normative evaluation is outside the scope of Research II.

### 7.2 No Empirical Claim Without Evidence

No claim about a specific system's function or authority distribution is made without documentary evidence. Where evidence is unavailable, the claim is marked as **unverified**.

### 7.3 Reproducibility

All document analysis is reproducible from publicly available sources. Coding decisions are documented in `ANALYSIS/coding_log.md`.

### 7.4 Limitations

- **Documentation bias:** Systems may under-document their functions and authorities.
- **Temporal bias:** Policies change; findings are dated to the analysis period.
- **System selection bias:** Four systems are not representative of all AI-mediated systems.

---

## 8. What This Methodology Does Not Do

- It does **not** examine user behavior directly.
- It does **not** conduct interviews or surveys.
- It does **not** access proprietary systems without documentation.
- It does **not** make normative claims about authority distribution.
- It does **not** integrate Research I findings (RQ-D1 remains deferred).

---

## 9. Alignment with Research Questions

| Family | Questions | Methodology |
|---|---|---|
| **A** | RQ-A1, RQ-A2, RQ-A3 | Document Analysis (Phase 1) + Comparative Analysis (Phase 3) |
| **B** | RQ-B1–RQ-B6 | Document Analysis (Phase 1) + Comparative Analysis (Phase 3) |
| **C** | RQ-C1–RQ-C5 | Case Study (Phase 2) + Comparative Analysis (Phase 3) |
| **D** | RQ-D1 (deferred), RQ-D2 (this document) | — |

---

## 10. Document Status

| Field | Value |
|---|---|
| Version | 0.2 |
| Status | ✅ Adopted |
| Date | 2026-11-04 |
| Methodology | Mixed Methods (Document Analysis → Case Study → Comparative Analysis) |
| Primary Systems | 4 (ChatGPT, Gemini, Claude, Perplexity) |
| Case Study System | 1 (ChatGPT) |
| Timeline | 10–14 weeks total |
| Next | Phase 1 — Document Analysis |
