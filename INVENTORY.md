# Research II — Complete Inventory

**Version:** 0.1.0
**Release Date:** 2026-11-04
**Author:** Samir Baladi
**Email:** gitdeeper@gmail.com
**ORCID:** 0009-0003-8903-0029
**License:** MIT (code) · CC-BY-4.0 (docs, manuscript, figures)
**Status:** Architecture Specification Stage · Research protocol · No empirical results
**DOI (Zenodo):** 10.5281/zenodo.23940837
**DOI (OSF Registration):** 10.17605/OSF.IO/8NZV2
**DOI (Figshare):** 10.6084/m9.figshare.34908597
**OSF Project:** osf.io/vmx2u

---

## Repository Links

| Platform | URL | Role |
|----------|-----|------|
| GitHub | https://github.com/gitdeeper15/pcr-ai | Primary |
| GitLab | https://gitlab.com/gitdeeper/pcr-ai | Mirror |
| Codeberg | https://codeberg.org/gitdeeper/pcr-ai | Mirror |
| Bitbucket | https://bitbucket.org/gitdeeper/pcr-ai | Mirror |
| PyPI | https://pypi.org/project/pcr-ai | Python package |
| Zenodo | https://doi.org/10.5281/zenodo.23940837 | DOI (manuscript archive) |
| OSF Registration | https://doi.org/10.17605/OSF.IO/8NZV2 | Registration |
| OSF Project | https://osf.io/vmx2u | Associated project |
| Internet Archive | https://archive.org/details/osf-registrations-8nzv2-v1 | Permanent copy |
| Figshare | https://doi.org/10.6084/m9.figshare.34908597 | Secondary archive |
| Website | https://pcr-ai.netlify.app | Live documentation |
| ORCID | https://orcid.org/0009-0003-8903-0029 | Identity |

---

## Root Files

| File | Purpose |
|------|---------|
| `.gitignore` | Git ignore rules |
| `AUTHORS.md` | Contributors |
| `CHANGELOG.md` | Version history |
| `CITATION.cff` | Citation metadata |
| `CONTRIBUTING.md` | Contribution guidelines |
| `INVENTORY.md` | Complete inventory |
| `LICENSE` | MIT + CC-BY-4.0 |
| `OSF_REGISTRATION.md` | OSF registration record |
| `PROJECT_SUMMARY.txt` | One-page summary |
| `README.md` | Main documentation |
| `VERSION` | 0.1.0 |
| `manifest.json` | Project manifest |
| `scientific_state.json` | Scientific state record |
| `requirements.txt` | Python deps |
| `setup.cfg` | Setup config |
| `setup.py` | Package setup |
| `upload_pcr.py` | PyPI uploader |

---

## Directories

| Directory | Purpose |
|-----------|---------|
| `PUBLICATION/` | Manuscript, figures, Netlify |
| `DATA/` | Data (raw, processed, schemas) |
| `ANALYSIS/` | Analysis notes, templates |
| `REPORTS/` | Governance/audit reports |
| `EXTERNAL_REVIEW/` | Review records |
| `VALIDATION/` | Validation checks, schemas |
| `docs/` | Foundational documents (4) + iteration log |
| `protocol/` | Methodological scope |
| `literature/` | Literature review (4 stages) |
| `figures/` | Conceptual diagrams (4) |

---

## Foundational Documents (docs/)

| Document | Version | Status |
|---|---|---|
| Conceptual Architecture | 0.2 | ✅ Adopted |
| Authority Structure | 0.2 | ✅ Adopted |
| Representation Lifecycle | 0.2 | ✅ Adopted |
| Research Questions | 0.2 | ✅ Adopted |

---

## Five Functional Units

| Unit | Function |
|------|----------|
| Producer | Originates or supplies representational material |
| Model / Generative System | Transforms inputs into a representation |
| Platform / Controller | Governs conditions of production, presentation, availability |
| Distribution Interface | Determines how representation reaches recipient |
| Recipient / Consumer | Receives and engages with representation |

---

## Five Authority Types

| Authority | Object | Central Question |
|-----------|--------|------------------|
| Production | The representation as originated | Who originates? |
| Transformation | The representation as modified | Who modifies? |
| Selection | The representation as presented | Who shows/hides? |
| Distribution | The representation as available | Who grants access? |
| Interpretive | The representation as interpreted | Whose meaning counts? |

---

## Six Lifecycle Stages

| Stage | Description |
|-------|-------------|
| 1. Origination | Representation constituted from material |
| 2. Transformation | Representation modified or regenerated |
| 3. Selection | Representation included in/excluded from presented set |
| 4. Distribution | Representation made available (or restricted) |
| 5. Reception | Representation reaches recipient |
| 6. Re-origination | Recipient produces new representation (distinct category) |

---

## Five Alternative Lifecycle Paths

| Path | Structure |
|------|-----------|
| Canonical | Origination → Transformation → Selection → Distribution → Reception → Re-origination |
| Merged | [Origination + Transformation + Selection + Distribution] → Reception |
| Skipped Transformation | Origination → Selection → Distribution → Reception |
| Skipped Selection | Origination → Transformation → Distribution → Reception |
| Distributed Origination | [Producer₁ + Producer₂ + … + Producerₙ] → Transformation → … |
| Iterative Re-origination | Origination → … → Reception → Re-origination → Transformation → … |

---

## Twenty Research Questions (4 families)

| Family | Questions | Focus |
|--------|-----------|-------|
| A — Conceptual | RQ-A1, RQ-A2, RQ-A3 | The analytical categories themselves |
| B — Authority | RQ-B1 – RQ-B6 | The distribution and exercise of authority |
| C — Lifecycle | RQ-C1 – RQ-C5 | The paths and interruptions of representations |
| D — Boundary | RQ-D1, RQ-D2 | Relation to Research I and methodological scope |

---

## Literature Review (4 stages)

| Stage | Focus | Status |
|-------|-------|--------|
| Stage 1 | Categorical positioning (16 categories × 5 traditions) | ✅ Completed |
| Stage 2 | Reference-level verification (56 references) | ✅ Completed |
| Stage 2b | Targeted verification of Distinct categories | ✅ Completed |
| Stage 3 | Synthesis draft (Section 2) | ✅ Draft complete |

---

## Methodological Scope (v0.2 — Adopted)

| Approach | Role | Systems |
|---|---|---|
| Document Analysis | Primary | ChatGPT, Gemini, Claude, Perplexity |
| Case Study | Secondary | ChatGPT |
| Comparative Analysis | Tertiary | All four systems |

**Timeline:** 10–14 weeks (Phase 1: 4–6, Phase 2: 3–4, Phase 3: 3–4)

---

## Dependencies

### Python (runtime)

- None at protocol stage

### Python (future empirical work, RQ-D2)

- `numpy >= 1.24.0`
- `pandas >= 2.0.0`
- `scikit-learn >= 1.3.0`

### External APIs

- None (protocol stage; no API calls).

---

## Completion Summary

```

Project: Research II — The Production and Control of Representations in Artificial Intelligence
Version: 0.1.0
Status: Architecture Specification Stage · Research protocol · No empirical results
Functional Units: 5
Authority Types: 5
Lifecycle Stages: 6
Alternative Paths: 5
Research Questions: 20 (4 families)
Literature Review: 4 stages completed
Methodological Scope: v0.2 (adopted)
Empirical Evaluation: Not executed
Causal Claims: None (research protocol)
License: MIT (code) + CC-BY-4.0 (manuscript, figures, docs)

```

---

## Citation

```bibtex
@techreport{baladi2026research2,
  author       = {Baladi, Samir},
  title        = {The Production and Control of Representations in Artificial Intelligence --- Research II: A Conceptual Architecture, Authority Structure, Representation Lifecycle, and Research Protocol},
  institution  = {Ronin Institute / Rite of Renaissance},
  type         = {Research Protocol},
  year         = {2026},
  month        = {November},
  version      = {0.1.0},
  doi          = {10.5281/zenodo.23940837},
  url          = {https://doi.org/10.5281/zenodo.23940837},
  note         = {Initial Program Manuscript --- Architecture Specification Stage.
                  All four foundational documents adopted (v0.2).}
}
```

---

Generated: 2026-11-04
Inventory Version: 0.1.0
