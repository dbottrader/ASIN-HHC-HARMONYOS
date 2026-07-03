# Artifact Migration Plan

This plan defines how remaining ASIN-HHC / CP8 project files should be moved into the repository.

---

## 1. Migration Priority

### Priority 1 — Canonical Documents

Move high-level documents first:

- CP8 ecosystem consolidated archive.
- HarmonyOS mapping reports.
- Provenance documents.
- Architecture documents.
- Evidence and witness handoff packages.

Target paths:

```text
docs/
witness/
archive/reports/
```

### Priority 2 — Machine-Readable Data

Move JSON manifests, audit packets, hashes, and structured bundles.

Target paths:

```text
manifests/
archive/json/
verification/hashes/
```

### Priority 3 — UI Artifacts

Move single-file HTML tools, visualizers, and interfaces.

Target paths:

```text
public/ui/
public/visualizers/
public/codex/
```

### Priority 4 — Scripts and Reproduction Harnesses

Move Python, JavaScript, validation scripts, Merkle builders, benchmark harnesses, and test files.

Target paths:

```text
scripts/
verification/scripts/
research/scripts/
```

### Priority 5 — Images, PDFs, and Media

Move visual/codex assets only with provenance notes.

Target paths:

```text
assets/images/
assets/pdf/
assets/media/
```

---

## 2. Known Artifacts To Migrate

- `CP8_PHI_BUNDLE_20260627_Master.json`
- `CP8_PHI_BUNDLE_20260627_v2.3_Master.json`
- `CP8_CONV_CRIT_005_Convergent_Critique.json`
- `PRED-003-v2.3 benchmark harness`
- `Weaver Epistemic Promotion Gate v1.2`
- `Cathedral spine MVP0 witness handoff`
- `Shock Kernel witness package template`
- `Cycle 010 Workflow UI`
- `DIGMA COUSA 28-Glyph OS`
- `ASIN Handshake Image Engine`
- `CCD-9 Formation 791 Codex Page`
- `Buga/Boga sphere glyph grammar analysis`

---

## 3. Required Metadata Per Artifact

Each migrated artifact should include:

```text
title:
source:
date:
artifact_type:
evidence_class:
path:
hash:
boundary:
next_step:
```

---

## 4. Migration Boundary

Migration into the repository means preservation and traceability. It does not automatically promote an artifact into a higher evidence class.
