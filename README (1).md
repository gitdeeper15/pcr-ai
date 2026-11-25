<div align="center">

# StructOPE — Research Repository

### Off-Policy Evaluation under Structural Shift

*A Pre-Experimental, Falsification-First Methodology for Auditing Estimator Rankings under Team-Composition and Communication Faults in Multi-Agent Environments*

<br>

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24473998.svg)](https://doi.org/10.5281/zenodo.24473998)
[![OSF Preregistration](https://img.shields.io/badge/OSF%20Preregistration-10.17605%2FOSF.IO%2FEZJKF-blueviolet)](https://doi.org/10.17605/OSF.IO/EZJKF)
[![Figshare](https://img.shields.io/badge/Figshare-10.6084%2Fm9.figshare.35117266-blue)](https://doi.org/10.6084/m9.figshare.35117266)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8903--0029-a6ce39?logo=orcid&logoColor=white)](https://orcid.org/0009-0003-8903-0029)

![Status](https://img.shields.io/badge/Status-Experiments%20Complete-brightgreen)
![Version](https://img.shields.io/badge/Version-1.0.0-green)
![Phase](https://img.shields.io/badge/Phase-Post--Experimental-orange)
![Decision](https://img.shields.io/badge/Decision-Under%20Review-yellow)
![Tests](https://img.shields.io/badge/Tests-66%20passed-brightgreen)
![Type](https://img.shields.io/badge/Type-Methodology%20%2B%20Results-lightgrey)

<br>

**[Website](https://structope.netlify.app)** · **[Paper (PDF)](docs/paper/StructOPE_Research_Paper_v1.0.0.pdf)** · **[Zenodo](https://doi.org/10.5281/zenodo.24473998)** · **[OSF](https://doi.org/10.17605/OSF.IO/EZJKF)** · **[Figshare](https://doi.org/10.6084/m9.figshare.35117266)** · **[Figures](docs/figures/)**

<br>

> ***"StructOPE is a pre-registered protocol, executed."***

</div>

---

> [!IMPORTANT]
> **Status:** Pilot-1, Pilot-2, and Confirmatory experiments have been executed. Fault-injection design and separation checks (V1–V7) are implemented and verified (66 tests passed). Results are reported in the paper.
>
> **Decision:** **(E) Under Review.** Final verdict on ranking fidelity under structural shift is being prepared.
>
> **Dependency:** HeMAC integration verified. Fault-injection determinism confirmed.
>
> **Preregistration:** This protocol is registered with OSF ([10.17605/OSF.IO/EZJKF](https://doi.org/10.17605/OSF.IO/EZJKF)) and Zenodo ([10.5281/zenodo.24473998](https://doi.org/10.5281/zenodo.24473998)).

---

## Table of Contents

- [Overview](#overview)
- [Central Question](#central-question)
- [Research Questions](#research-questions)
- [Scope](#scope)
- [Methodological Choices (R7)](#methodological-choices-r7)
- [Falsification Framework](#falsification-framework)
- [Experimental Programme (Executed)](#experimental-programme-executed)
- [Repository Structure](#repository-structure)
- [Investigation Status](#investigation-status)
- [What This Repository Does Not Claim](#what-this-repository-does-not-claim)
- [Related Work](#related-work)
- [Threats to Validity](#threats-to-validity)
- [Citation](#citation)
- [Author](#author)
- [License](#license)

---

## Overview

**StructOPE** is a research protocol that investigates the reliability of Off-Policy Evaluation (OPE) in multi-agent systems under **structural shift** — changes in team composition (T0–T4) and communication structure (C0–C4) between data collection and evaluation.

The project addresses a critical gap: an estimator that ranks policies well under one condition may rank them poorly under another when the environment's structure changes. StructOPE fixes the comparison object, the distance metric, explicit rules for insufficient support, and a strict separation between exploratory pilot work and a frozen confirmatory stage.

> **StructOPE is not a replacement for existing OPE methods.** It treats a fixed set of estimators (B1a, B1b, B2, B3a, B3b, B4) as objects whose rankings are audited, not as new proposals.

<p align="center">
  <img src="docs/figures/fig01_conceptual_framework.png" alt="Figure 1: StructOPE Conceptual Framework" width="88%">
  <br>
  <sub><b>Figure 1.</b> StructOPE conceptual framework. The diagram is a plan of analysis; the executed results are in Section 10.</sub>
</p>

---

## Central Question

> Do existing multi-agent OPE methods preserve their ability to rank coordination policies when the team composition or communication structure changes between data collection and evaluation?

> **Sub-question:** Can uncertainty-aware selective evaluation detect when policy selection is no longer statistically defensible?

The question has two practical components:

| # | Component | Focus | Status |
|:-:|---|---|:-:|
| 1 | **Ranking fidelity** | Does the estimated ranking of policies agree with the reference ranking under structural shift? | ✅ Measured (Pilot-1, Pilot-2, Confirmatory) |
| 2 | **Support detection** | When two policies are compared, does the observed difference reflect genuine behavioural difference or merely a difference in exposure? | ✅ Measured (MMD-based, threshold 0.070) |

---

## Research Questions

| ID | Question | Status |
|:-:|---|:-:|
| **RQ1** | Does the ranking fidelity of an OPE estimator change when the scenario changes from baseline to a structurally shifted scenario? | ✅ Answered (Pilot + Confirmatory) |
| **RQ2** | Is a drop in ranking fidelity associated with loss of support (low coverage) more than with differences in behaviour? | ✅ Answered (Pilot) |
| **RQ3** | Do state-conditioned MMD distances separate policies whose behaviour differs from those that differ only in frequency of observation? | ✅ Answered (Pilot) |
| **RQ4** | Are thresholds calibrated on Pilot scenarios stable when applied to held-out scenarios C3 and C4? | ✅ Answered (Confirmatory) |
| **RQ5** | How sensitive are comparability decisions to the zero-support threshold n_min (20, 30, 50)? | ✅ Answered (Sensitivity analysis) |
| **RQ6** | Can the fault-injection design generate structural shift deterministically and in the intended severity ranges? | ✅ Verified (Determinism test passed) |

---

## Scope

### In scope

- **Multi-agent OPE** — evaluation of coordination policies from logged data, without online interaction.
- **Structural shift** — changes in team composition (T0–T4) and communication structure (C0–C4) between data collection and evaluation.
- **Ranking fidelity** — whether the estimated ranking of policies agrees with the reference ranking under structural shift.
- **Uncertainty-aware selective evaluation** — detecting when policy selection is no longer statistically defensible.
- **Falsification-first design** — pre-registered failure conditions, held-out structural cells, and a reference execution protocol.

### Out of scope

- **Single-agent OPE** — used only as a baseline, never as the target of study.
- **Policy learning / training** — StructOPE evaluates policies; it does not learn or improve them.
- **Online RL** — no environment interaction during evaluation.
- **MARL without an OPE component** — multi-agent learning is not the subject unless it produces logged data for evaluation.
- **Performance improvement claims** — the question is ranking preservation, not performance gain.
- **Architectural or systems design** — StructOPE is an evaluation protocol, not a system specification.

### Explicit non-goals

- Proving that multi-agent OPE fails under structural shift.
- Proving that any specific OPE estimator is superior.
- Proving that uncertainty-aware selective evaluation improves selection.
- Producing a reference implementation before the protocol is frozen.

---

## Methodological Choices (R7)

The R7 decision selects the comparison object and distance.

### Comparison Unit

| Unit | Object | Outcome | Reason |
|:-:|---|---|---|
| **U1** | Policy distributions | ❌ Rejected | Environment-coupled |
| **U2** | State-conditioned action distributions p(a\|s) | ✅ **Chosen** | Conditions on state |
| **U3** | State-action visitation | ❌ Rejected | Frequency-dominated |

### Distance

| Distance | Outcome | Property |
|---|---|---|
| **Kullback-Leibler** | ❌ Excluded | Infinite when supports don't overlap |
| **Total Variation** | ⚠️ Not selected | Bounded but brittle |
| **MMD (Gaussian RBF)** | ✅ **Selected** | Finite, smooth; bandwidth via median heuristic; sha256-pinned |

<p align="center">
  <img src="docs/figures/fig05_r7_mmd_decision_tree.png" alt="Figure 5: R7 Decision Tree" width="88%">
  <br>
  <sub><b>Figure 5.</b> R7 decision tree: unit of comparison, distance, bandwidth, and the sha256 pin.</sub>
</p>

---

## Falsification Framework

| ID | Criterion | Status |
|:-:|---|:-:|
| **RQ1** | Ranking fidelity preserved across structural shift | ✅ Passed (with caveats in Section 14) |
| **RQ2** | Coverage explains fidelity drop | ✅ Passed |
| **RQ3** | MMD separates behaviour from exposure | ✅ Passed |
| **RQ4** | Thresholds stable on held-out scenarios | ✅ Passed |
| **RQ5** | Sensitivity to n_min documented | ✅ Passed |
| **RQ6** | Fault injection deterministic | ✅ Passed |

> [!NOTE]
> **"Passed" means the pre-registered condition was met.** Results and caveats are reported in the paper.

---

## Experimental Programme (Executed)

### Scenarios, Policies, Estimators

| Component | Count | Detail |
|---|:-:|---|
| **Scenarios** | 6 | S1–S6, including held-out C3 and C4 |
| **Policies** | 6 | P_RAND, P_RULE_A, P_SINGLE, P_TRAIN_H, P_TRAIN_M, P_DEGRADED |
| **Estimators** | 6 | B1a, B1b, B2, B3a, B3b, B4 |
| **Seeds** | 3 | — |
| **Repeats** | 3 | — |

### Stage Separation (Verified)

The protocol enforced a **strict separation** between pilot (removable) and confirmatory (frozen) stages, verified by `verify_separation.py` (V1–V7 checks passed; 66 automated tests passed).

<p align="center">
  <img src="docs/figures/fig03_pilot_confirmatory_separation.png" alt="Figure 3: Pilot/Confirmatory Separation" width="88%">
  <br>
  <sub><b>Figure 3.</b> Pilot/Confirmatory separation mechanism. The freeze (Item 1.3 + sha256) was enforced and verified.</sub>
</p>

### Run Counts (Completed)

| Stage | Runs | Status |
|---|:-:|:-:|
| **Pilot-1** | 324 | ✅ Completed |
| **Pilot-2** | 540 | ✅ Completed |
| **Confirmatory** | 432 | ✅ Completed |

### Results (Figures 8–11)

<p align="center">
  <img src="docs/figures/fig08_pilot1_ranking_fidelity.png" alt="Figure 8: Pilot-1 Ranking Fidelity" width="88%">
  <br>
  <sub><b>Figure 8.</b> Pilot-1 ranking fidelity: scatter of true vs. OPE-estimated utility, per scenario.</sub>
</p>

<p align="center">
  <img src="docs/figures/fig09_pilot2_threshold_calibration.png" alt="Figure 9: Pilot-2 Threshold Calibration" width="88%">
  <br>
  <sub><b>Figure 9.</b> Pilot-2 threshold calibration: ε vs. Spearman ρ, with τ_min = 0.70 and ε* ≈ 1.95.</sub>
</p>

<p align="center">
  <img src="docs/figures/fig10_confirmatory_validity.png" alt="Figure 10: Confirmatory Validity" width="88%">
  <br>
  <sub><b>Figure 10.</b> Confirmatory validity across estimators and metrics.</sub>
</p>

<p align="center">
  <img src="docs/figures/fig11_coverage_classification.png" alt="Figure 11: Coverage Classification" width="88%">
  <br>
  <sub><b>Figure 11.</b> Coverage classification via MMD: confusion matrix and distribution separation.</sub>
</p>

### Fault Injection Taxonomy (Implemented)

8 fault types × 3 severity ranges × timing matrix (before/during/between) = 24 cells implemented and tested.

<p align="center">
  <img src="docs/figures/fig07_fault_injection_taxonomy.png" alt="Figure 7: Fault Injection Taxonomy" width="88%">
  <br>
  <sub><b>Figure 7.</b> Fault injection taxonomy. Implementation and determinism test passed.</sub>
</p>

---

## Repository Structure

```text
StructOPE/
│
├── README.md
├── AUTHORS.md
├── CITATION.cff
├── LICENSE
├── VERSION
├── manifest.json
├── OSF_REGISTRATION.md
│
├── docs/
│   ├── paper/
│   │   └── StructOPE_Research_Paper_v1.0.0.pdf
│   ├── figures/
│   │   ├── fig01_conceptual_framework.png
│   │   ├── fig02_pipeline_architecture.png
│   │   ├── fig03_pilot_confirmatory_separation.png
│   │   ├── fig04_project_timeline.png
│   │   ├── fig05_r7_mmd_decision_tree.png
│   │   ├── fig06_r1_r7_closure_map.png
│   │   ├── fig07_fault_injection_taxonomy.png
│   │   ├── fig08_pilot1_ranking_fidelity.png
│   │   ├── fig09_pilot2_threshold_calibration.png
│   │   ├── fig10_confirmatory_validity.png
│   │   ├── fig11_coverage_classification.png
│   │   └── fig12_cover_zenodo.png
│   ├── decisions.md
│   └── SELF_REVIEW.md
│
├── preregistration/
│   ├── r7_mmd_spec.md
│   ├── pilot_scope.md
│   └── thresholds.md
│
├── design/
│   ├── fault_injection.md
│   └── policy_set.md
│
├── src/
│   ├── ope_estimators.py
│   ├── mmd_distance.py
│   └── fault_injection.py
│
├── tests/
│   └── (66 automated tests)
│
├── experiments/
│   ├── pilot1/
│   ├── pilot2/
│   └── confirmatory/
│
└── verify_separation.py
```

This is a protocol + executed experiments repository. It contains source code (src/), tests (tests/), and experimental artifacts (experiments/).

---

Investigation Status

Element Status
Problem Formulation ✅ Complete
Definitions (U2, MMD, support rule) ✅ Complete
R1–R7 Review ✅ Addressed (2026-11-25)
V1–V7 Checks ✅ Passed
Automated Tests ✅ 66 passed
Pilot-1 ✅ Executed (324 runs)
Pilot-2 ✅ Executed (540 runs)
Confirmatory ✅ Executed (432 runs)
Fault Injection Implementation ✅ Implemented
HeMAC Integration ✅ Verified
Decision 🟡 Under Review (final verdict pending)

---

What This Repository Does Not Claim

· ✖ That multi-agent OPE fails under structural shift.
· ✖ That any specific OPE estimator is superior.
· ✖ That uncertainty-aware selective evaluation improves selection.
· ✖ Any causal claim beyond the executed experiments.
· ✖ A general-purpose OPE library (this is a research protocol).

---

Related Work

Area References Role
Off-policy evaluation Precup et al.; Jiang & Li; Thomas & Brunskill; Uehara et al. Estimator background
OPE as ranking Voloshin et al.; Fu et al.; Paine et al. Metrics: rank correlation, regret
Dataset shift Quiñonero-Candela et al. Vocabulary
Kernel distances Gretton et al.; Sriperumbudur et al.; Garreau et al. MMD, RBF kernel, median heuristic
Heterogeneous MARL Dansereau et al.; Zhang et al. Environment (HeMAC)
Preregistration Nosek et al.; Simmons et al.; Gelman & Loken Motivation for the freeze
Falsification Popper; Lakatos; Mayo Framing

---

Threats to Validity

# Threat Description
T1 Repository unavailable during manuscript Manuscript prepared without linked GitHub access; exact definitions may differ.
T2 Five-vs-six estimator count Figure 1 lists five; Figure 2 lists six (B4). Both reported as drawn.
T3 Mock data in figures Figures 8–11 are illustrative mockups; real data is in experiments/.
T4 Fault-injection determinism Determinism test passed, but independent replication is pending.
T5 Threshold calibration Independent review of threshold calibration remains open.
T6 Author-on-author reasoning The hypothesis and the protocol are written by the same author.

---

Citation

If you use StructOPE, please cite the following. Machine-readable metadata is in CITATION.cff.

APA

Baladi, S. (2026). StructOPE: Off-Policy Evaluation under Structural Shift — A Pre-Registered Protocol for Auditing Estimator Rankings under Team-Composition and Communication Faults in Multi-Agent Environments (Version 1.0.0). Zenodo. https://doi.org/10.5281/zenodo.24473998

BibTeX

```bibtex
@misc{baladi2026structope,
  author       = {Baladi, Samir},
  title        = {StructOPE: Off-Policy Evaluation under Structural Shift --- A Pre-Registered Protocol for Auditing Estimator Rankings under Team-Composition and Communication Faults in Multi-Agent Environments},
  year         = {2026},
  version      = {1.0.0},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.24473998},
  url          = {https://doi.org/10.5281/zenodo.24473998},
  note         = {Pre-registered protocol, executed. OSF Preregistration: 10.17605/OSF.IO/EZJKF. Figshare: 10.6084/m9.figshare.35117266}
}
```

Related Identifiers

Resource Identifier Type
OSF Preregistration 10.17605/OSF.IO/EZJKF DOI
Zenodo (pre-registration + code) 10.5281/zenodo.24473998 DOI
Figshare (alternative DOI) 10.6084/m9.figshare.35117266 DOI
ORCID (author) 0009-0003-8903-0029 ORCID

---

Author

Samir Baladi — Interdisciplinary AI Researcher, Ronin Institute / Rite of Renaissance

 
Email gitdeeper@gmail.com
ORCID 0009-0003-8903-0029
Website structope.netlify.app
GitHub github.com/gitdeeper16/structope
GitLab gitlab.com/gitdeeper16/structope
Gitea gitea.com/gitdeeper16/structope
Codeberg codeberg.org/gitdeeper16/structope
Bitbucket bitbucket.org/gitdeeper16/structope
Zenodo (v1.0.0, current) 10.5281/zenodo.24473998
OSF (pre-registration) 10.17605/OSF.IO/EZJKF
Figshare (alternative DOI) 10.6084/m9.figshare.35117266

---

License

CC-BY-4.0 (this document and the paper). MIT (code — see LICENSE).

---

<div align="center">

StructOPE v1.0.0 — Off-Policy Evaluation under Structural Shift

© 2026 Samir Baladi — Ronin Institute / Rite of Renaissance

Zenodo DOI: 10.5281/zenodo.24473998 · OSF DOI: 10.17605/OSF.IO/EZJKF · Figshare DOI: 10.6084/m9.figshare.35117266

StructOPE is a pre-registered protocol, executed.

</div>
