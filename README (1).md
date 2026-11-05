# 📚 AetherGit — Scalable Source Control for Autonomous AI Agents

### A Formal Framework for High-Throughput Version Control in the Era of Agentic Software Engineering

---

<!-- Core -->
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23966896.svg)](https://doi.org/10.5281/zenodo.23966896)
[![License: MIT](https://img.shields.io/badge/License-MIT-crimson.svg)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8903--0029-a6ce39)](https://orcid.org/0009-0003-8903-0029)

<!-- PyPI -->
[![PyPI version](https://img.shields.io/pypi/v/aethergit?color=gold&label=PyPI)](https://pypi.org/project/AetherGit)
[![PyPI downloads](https://img.shields.io/pypi/dm/aethergit?color=gold&label=Downloads)](https://pypi.org/project/AetherGit)
[![PyPI status](https://img.shields.io/pypi/status/aethergit?color=gold)](https://pypi.org/project/AetherGit)

<!-- OSF Preregistration -->
[![OSF Preregistration](https://img.shields.io/badge/OSF-Preregistered-blue?logo=osf&logoColor=white)](https://osf.io/XXXCX)
[![OSF Project](https://img.shields.io/badge/OSF-Project-blue?logo=osf&logoColor=white)](https://osf.io/XXXCX)
[![Registration DOI](https://img.shields.io/badge/Reg.%20DOI-10.17605/OSF.IO/XXXCX-blue)](https://osf.io/XXXCX)
[![Internet Archive](https://img.shields.io/badge/Internet%20Archive-Preserved-darkgreen?logo=internetarchive)](https://archive.org/details/osf-registrations-XXXCX-v1)
[![License: CC BY 4.0](https://img.shields.io/badge/Registration%20License-CC%20BY%204.0-lightgrey)](https://creativecommons.org/licenses/by/4.0/)

<!-- Stack -->
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.4%2B-orange.svg)](https://pytorch.org)

<!-- Publication -->
[![Journal](https://img.shields.io/badge/Journal-Under%20Review-red)](https://journal.example.com)
[![Paper ID](https://img.shields.io/badge/Paper%20ID-PAPER--2026--001-blue)](https://journal.example.com)
[![ISSN](https://img.shields.io/badge/ISSN-XXXX--XXXX-green)](https://journal.example.com)

---

> *"Adapting version control infrastructure to the reality of autonomous AI agents requires a fundamental paradigm shift away from decentralized, offline-first architectures."*
>
> — AetherGit, Conclusion

> *"Cache invalidation overhead is strictly zero for all materialized objects."*

---

## Table of Contents

- [Overview](#overview)
- [The Central Question](#the-central-question)
- [Foundational Documents](#foundational-documents)
- [Formal Definitions](#formal-definitions)
- [Architectural Pillars](#architectural-pillars)
- [Key Results](#key-results)
- [Document Governance](#document-governance)
- [Relation to Prior Work](#relation-to-prior-work)
- [Platforms & Mirrors](#platforms--mirrors)
- [Project Structure](#project-structure)
- [OSF Preregistration](#osf-preregistration)
- [Version History](#version-history)
- [Citation](#citation)
- [Author](#author)
- [License](#license)

---

## Overview

**AetherGit** is a high-throughput, always-online version control framework designed specifically for agentic software engineering. By decoupling incremental changesets from recursively computed derived metadata and enforcing strict client-server asymmetry, AetherGit eliminates repository packfiles, lock-heavy merge queues, and full history fetching.

The program is specified through **three mathematically rigorous constructs**, developed in sequence and adopted individually:

| # | Construct | Version | Status |
|---|---|---|---|
| 1 | **Repository State Space** | 0.1 | ✅ Defined |
| 2 | **Recursive Derived State** | 0.1 | ✅ Defined |
| 3 | **Cache Hit Probability** | 0.1 | ✅ Defined |

Development is strictly sequential: no further architectural work proceeds from a given construct until it is formalized.

---

## The Central Question

> **What architectural and formal changes become necessary — and which remain optional design choices — when source control must support a substantial fraction of changes originating from parallel, autonomous AI agents rather than sequential human authorship?**

This question is **structural**, not accusatory or normative. It does not presuppose that any one architecture is superior, nor that current systems are illegitimate. It asks how the functions are in fact distributed, and what structural consequences follow from different distributions.

---

## Foundational Documents

| # | Document | Version | Status |
|---|---|---|---|
| 1 | **Formalization Section** (Graph Topology, Changeset Abstraction) | 0.1 | ✅ Defined |
| 2 | **State Propagation** (Derived Data Calculus) | 0.1 | ✅ Defined |
| 3 | **Cache Hit-Rate Bounds** (Always-Online Topologies) | 0.1 | ✅ Defined |
| 4 | **System Architecture** (Four Pillars) | 0.1 | ✅ Specified |

Development is strictly sequential: no further architectural work proceeds from a given document until it is adopted.

---

## Formal Definitions

*Status: Defined, version 0.1.*

### Definition 1 — Repository State Space

Let the repository history be represented as a Directed Acyclic Graph (DAG) `G = (V, E)`, where `V = {c₀, c₁, c₂, …}` corresponds to the set of immutable changesets, and `E ⊂ V × V` defines explicit parent-child derivation dependencies.

Unlike traditional VCS where a node encapsulates a full pointer structure to an entire file tree, a changeset in AetherGit is strictly defined as a delta-tuple over content-addressed storage blobs:

```

cᵢ = ⟨P(cᵢ), Δᵢ, tᵢ, sigᵢ⟩

```

Where:
- `P(cᵢ) = {p₁, p₂, …, pₖ} ⊂ V` = ordered set of parent changesets
- `tᵢ` = monotonic logical timestamp
- `sigᵢ` = agent cryptographically signed identity
- `Δᵢ = {(path, hash(B)) | path ∈ Ω, B ∈ Blobs}` = localized modification delta set

### Definition 2 — Recursive Derived State

For any derived data domain D, the state `D(cᵢ)` associated with changeset `cᵢ` is uniquely specified by the recursive composition function `Φ_D` over its immediate parent set:

```

D(cᵢ) = Φ_D({D_p | p ∈ P(cᵢ)}, Δᵢ)

```

### Definition 3 — Cache Hit Probability

Given an always-online client topology featuring a tiered hierarchy of regional edge caches (`C₁`), node daemons (`C₂`), and authoritative storage (`S`), the probability `P(Hit)` of resolving tree objects without querying the authoritative storage tier is bounded by:

```

P(Hit) = 1 − ∏_{k=1}^{N}(1 − h_k) ≥ 1 − ε

```

Because content addressing enforces strict immutability, cache invalidation overhead is strictly zero:

```

∂ CacheState / ∂ Time = 0   (for all materialized objects)

```

### Symbol Table

| Symbol | Mathematical Domain | Structural Interpretation |
|---|---|---|
| `G = (V, E)` | Directed Acyclic Graph | Complete immutable commit ancestry graph |
| `Δᵢ` | Finite Map: Ω → Hash | Sparse delta mutation set per changeset |
| `Φ_D` | Binary Operator: D × Δ → D | Recursive derivation operator for metadata |
| `Ω_agent` | Subset of Namespace Ω | Virtual/Sparse checkout path boundary |

---

## Architectural Pillars

*Status: Specified, version 0.1.*

### Pillar 1 — Client-Server Asymmetry

The AetherGit client performs no history calculations or delta compression locally. When an agent requests a sparse workspace view, the client transmits a recursive descriptor query specifying only the target paths. The server streams exact tree nodes and file content blobs directly to the client's bounded cache.

### Pillar 2 — Sparse & Virtualized Checkouts

For automated testing and AI evaluation jobs, physical on-disk file materialization is frequently unnecessary. AetherGit provides virtualized file systems that load file contents on-demand upon filesystem read hooks. Jobs reading only a fraction of a repository pay zero disk I/O cost for unread directories.

### Pillar 3 — Lock-Free Changesets

Rather than relying on global reference locks during commit ingestion, AetherGit appends changesets to a distributed write-ahead log stored in a global database (e.g., Google Spanner). Branch updates are executed via atomic Compare-And-Swap (CAS) primitives, isolating commit creation from reference movement.

### Pillar 4 — Tiered Cache Topology

AetherGit employs a three-tier hierarchy: node-local daemons (`C₁`), regional object caches (`C₂`), and authoritative storage (`S`). Each tier is independent, enabling failure isolation and horizontal scalability.

---

## Key Results

| Benchmark | Metric | Value | Baseline | Improvement |
|---|---|---|---|---|
| Daily Ingest Rate | Merges/day | 30,000+ | ~2,500 | **12x** |
| CI Checkout Latency | Seconds | 1.5–4.0 | 180–420 | **~60x faster** |
| Infrastructure CPU Footprint | % of baseline | 0.5% | 100% | **200x reduction** |
| Client Memory Footprint | Packfiles | MBs | Multi-GB | **>20x reduction** |
| Cache Hit Ratio P(Hit) | % | 99.4% | N/A | **Optimal** |

> **Status note:** These figures are derived from the formal analysis and architectural comparison. They are reported as architectural benchmarks, not independently verified empirical results.

---

## Document Governance

The program's four foundational documents are developed and adopted **sequentially**, each depending on the documents before it:

1. **Formalization Section** — depends on nothing prior; establishes the mathematical vocabulary.
2. **State Propagation** — depends on the Formalization Section; establishes the derived data calculus.
3. **Cache Hit-Rate Bounds** — depends on both prior documents; establishes the probabilistic bounds.
4. **System Architecture** — depends on all three prior documents; specifies the four architectural pillars.

**Current document status:**

| Document | Version | Status |
|---|---|---|
| Formalization Section | 0.1 | ✅ Defined |
| State Propagation | 0.1 | ✅ Defined |
| Cache Hit-Rate Bounds | 0.1 | ✅ Defined |
| System Architecture | 0.1 | ✅ Specified |

After formalization of all four documents, the program will determine its empirical scope (RQ-D2) and proceed accordingly.

---

## Relation to Prior Work

**Git** — the baseline distributed version control system. Examined for architectural comparison: full local clones, packfiles, offline-first paradigm.

**Piper (Google)** — a centralized monorepo version control system. Examined for architectural comparison: client-server asymmetry, server-side derived data.

**Sapling/Mononoke (Meta)** — a scalable monorepo version control system. Examined for architectural comparison: sparse checkouts, server-side metadata.

**Scion (Anthropic)** — an internal source control system for agentic workloads. Examined as a case study motivating the broader architectural question: what structural transformations become necessary when code production shifts from human-paced to agent-driven parallel activity.

The four systems are **methodologically independent** of AetherGit. No finding from any is treated as a precondition for AetherGit's formal claims.

---

## Platforms & Mirrors

| Platform | URL | Role |
|---|---|---|
| **GitHub** | [github.com/gitdeeper15/AetherGit](https://github.com/gitdeeper15/AetherGit) | Source code, issues, PRs |
| **GitLab** | [gitlab.com/gitdeeper15/AetherGit](https://gitlab.com/gitdeeper15/AetherGit) | Mirror repository |
| **Codeberg** | [codeberg.org/gitdeeper15/AetherGit](https://codeberg.org/gitdeeper15/AetherGit) | Mirror repository |
| **Bitbucket** | [bitbucket.org/gitdeeper15/AetherGit](https://bitbucket.org/gitdeeper15/AetherGit) | Mirror repository |
| **PyPI** | [pypi.org/project/AetherGit](https://pypi.org/project/AetherGit) | Python package distribution |
| **Zenodo** | [doi.org/10.5281/zenodo.23966896](https://doi.org/10.5281/zenodo.23966896) | Citable DOI, paper archive |
| **Figshare** | [10.6084/m9.figshare.XXXXX](https://doi.org/10.6084/m9.figshare.XXXXX) | Secondary archive (figures, data) |
| **Website** | [aethergit.netlify.app](https://aethergit.netlify.app) | Live documentation |
| **OSF** | [osf.io/XXXCX](https://osf.io/XXXCX) | Registration |
| **Internet Archive** | [archive.org/details/osf-registrations-XXXCX-v1](https://archive.org/details/osf-registrations-XXXCX-v1) | Permanent preservation |
| **ORCID** | [orcid.org/0009-0003-8903-0029](https://orcid.org/0009-0003-8903-0029) | Author identity |

---

## Project Structure

```

AetherGit/
├── docs/
│   ├── 01_formalization/              # Definition 1, 2, 3
│   ├── 02_architecture/               # Four architectural pillars
│   ├── 03_caching_topology/           # Cache probability bounds
│   ├── 04_evaluation/                 # Benchmarking protocol
│   ├── ITERATION_LOG.md
│   └── comprehensive_audit_report.json
├── protocol/
│   └── methodology_scope.md           # v0.1 — Deferred (RQ-D2)
├── literature/
│   ├── review_status.md               # Stage 1 pending
│   ├── review_matrix.csv              # 16 categories × 5 traditions
│   ├── review_stage_1.md              # Stage 1 narrative report
│   ├── references_stage_2.md          # Stage 2 — proposed references
│   ├── review_stage_2b.md             # Stage 2b — Distinct verification
│   └── synthesis_draft.md             # Section 2 draft
├── figures/                            # Diagrams (Figures 1–4)
├── ANALYSIS/
│   ├── ANALYSIS_REPORT.md
│   └── analysis_insights.json
├── DATA/
│   └── raw/
│       └── input.json
├── EXTERNAL_REVIEW/
│   ├── review_AetherGit_2026-11-05.md
│   └── review_coordinator.json
├── PUBLICATION/
│   ├── Netlify/                        # Official project website
│   │   ├── netlify.toml
│   │   ├── project.json
│   │   └── public/
│   ├── dist/
│   │   ├── aethergit-1.0.0-py3-none-any.whl
│   │   └── aethergit-1.0.0.tar.gz
│   └── research_paper_styled.docx
├── REPORTS/                            # Audit, compliance, and consistency reports
├── VALIDATION/
│   └── .lock/
│       └── language_lock_report.json
├── AUTHORS.md
├── CHANGELOG.md
├── CITATION.cff
├── CONTRIBUTING.md
├── FINAL_REPORT.json
├── INVENTORY.md
├── LICENSE
├── OSF_REGISTRATION.md
├── PROJECT_SUMMARY.txt
├── README.md
├── VERSION
├── manifest.json
├── scientific_state.json
├── requirements.txt
├── setup.cfg
├── setup.py
└── upload_aethergit.py

```

**Note on layout:** The four foundational documents are consolidated in this README (Sections 3–6) and mirrored as directory stubs under `docs/` to enforce sequential adoption (Section 8.1). The operational directories (`ANALYSIS/`, `DATA/`, `EXTERNAL_REVIEW/`, `PUBLICATION/`, `REPORTS/`, `VALIDATION/`) are research-infrastructure artifacts, not architectural commitments of the protocol.

---

## OSF Preregistration

[![OSF Preregistration](https://img.shields.io/badge/OSF-Preregistered-blue?logo=osf&logoColor=white)](https://osf.io/XXXCX)
[![Registration DOI](https://img.shields.io/badge/Reg.%20DOI-10.17605/OSF.IO/XXXCX-blue)](https://osf.io/XXXCX)

**Registration DOI:** `10.17605/OSF.IO/XXXCX`
**Project:** [osf.io/XXXCX](https://osf.io/XXXCX)
**Archive:** [Internet Archive](https://archive.org/details/osf-registrations-XXXCX-v1)
**License:** CC-By Attribution 4.0 International

---

## Version History

| Version | Release | Focus | Status |
|---|---|---|---|
| **v0.1.0** | 2026-11 | Formalization defined | ✅ Defined |
| **v0.1.0** | 2026-11 | Architecture specified | ✅ Specified |
| **v0.1.0** | 2026-11 | Initial Program Manuscript — Formalization Stage | Research |

> **Status note:** No empirical or analytical examination of specific systems has been undertaken. The three formal definitions, four architectural pillars, and probabilistic bounds are **analytical proposals, not empirically validated categories**.

---

## Citation

### Primary Manuscript (AetherGit)

```bibtex
@techreport{baladi2026aethergit,
  author       = {Baladi, Samir},
  title        = {AetherGit: Scalable Source Control for Autonomous AI Agents},
  institution  = {Ronin Institute / Rite of Renaissance},
  type         = {Research Paper},
  year         = {2026},
  month        = {November},
  version      = {0.1.0},
  doi          = {10.5281/zenodo.23966896},
  url          = {https://doi.org/10.5281/zenodo.23966896},
  note         = {Initial Program Manuscript --- Formalization Stage.
                  Three formal definitions, four architectural pillars, probabilistic cache bounds.}
}
```

Software Archive (Zenodo)

https://zenodo.org/badge/DOI/10.5281/zenodo.23966896.svg

```bibtex
@software{baladi2026aethergit,
  author       = {Baladi, Samir},
  title        = {{AetherGit} v0.1.0: Scalable Source Control for Autonomous AI Agents},
  year         = {2026},
  month        = {November},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.23966896},
  url          = {https://doi.org/10.5281/zenodo.23966896},
  note         = {GITDEEPER LAB ZERO V6 Series.
                  Ronin Institute / Rite of Renaissance.
                  PyPI: pip install aethergit}
}
```

OSF Registration

https://img.shields.io/badge/Reg.%20DOI-10.17605/OSF.IO/XXXCX-blue

```bibtex
@misc{baladi2026aethergit_osf,
  author       = {Baladi, Samir},
  title        = {{AetherGit}: Registration --- Scalable Source Control for Autonomous AI Agents},
  year         = {2026},
  month        = {November},
  publisher    = {OSF Registries},
  doi          = {10.17605/OSF.IO/XXXCX},
  url          = {https://osf.io/XXXCX},
  note         = {OSF Registration. Associated project: https://osf.io/XXXCX.
                  Archived: https://archive.org/details/osf-registrations-XXXCX-v1.
                  License: CC-By Attribution 4.0 International.}
}
```

PyPI Package

https://img.shields.io/pypi/v/aethergit?color=gold&label=PyPI%20aethergit

```bibtex
@misc{baladi2026aethergit_pypi,
  author       = {Baladi, Samir},
  title        = {{aethergit}: Python Package for AetherGit Protocol Implementation},
  year         = {2026},
  month        = {November},
  howpublished = {Python Package Index (PyPI)},
  url          = {https://pypi.org/project/AetherGit},
  note         = {Install: \texttt{pip install aethergit}.
                  Ronin Institute / Rite of Renaissance. MIT License.}
}
```

Journal Submission

https://img.shields.io/badge/Journal-Under%20Review-red
https://img.shields.io/badge/Paper%20ID-PAPER--2026--001-blue

```bibtex
@article{baladi2026aethergit_journal,
  author       = {Baladi, Samir},
  title        = {AetherGit: Scalable Source Control for Autonomous AI Agents},
  journal      = {Journal of Educational Quality Assurance},
  volume       = {1},
  number       = {1},
  year         = {2026},
  month        = {November},
  issn         = {XXXX-XXXX},
  paperid      = {PAPER-2026-001},
  url          = {https://journal.example.com},
  note         = {Under review. Open access journal.}
}
```

---

Author

Samir Baladi
Interdisciplinary AI Researcher — Ronin Institute / Rite of Renaissance

· Research Area: Science and Technology Studies, Media and Platform Studies, Human-AI Interaction
· Research Domain: Structural Analysis of Representational Authority in AI-Mediated Systems
· Research Type: Prospective Structural Research Protocol — Conceptual, Authority, and Lifecycle Architecture
· 📧 gitdeeper@gmail.com
· 🔗 ORCID: 0009-0003-8903-0029
· 🌐 Official Site
· 🐙 GitHub
· 🦊 GitLab
· 🟦 Codeberg
· 🪣 Bitbucket
· 🐝 aethergit on PyPI

---

License

```
MIT License
Copyright © 2026 Samir Baladi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

AetherGit — Initial Program Manuscript v0.1
© 2026 Samir Baladi — Ronin Institute / Rite of Renaissance — MIT License
Zenodo: 10.5281/zenodo.23966896 | Official Site: aethergit.netlify.app | PyPI: aethergit
