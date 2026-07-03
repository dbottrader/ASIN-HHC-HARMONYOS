# Research Library

This directory is for structured ASIN-HHC / CP8 research threads.

---

## Research Areas

### 1. Glyph Grammar

Goal: formalize glyphs into measurable feature vectors.

Potential features:

- symmetry;
- stroke count;
- radial count;
- loop count;
- intersection count;
- enclosure count;
- line/curve ratio;
- rotational order;
- adjacency graph;
- ASIN mapping.

### 2. Sphere / Object Analysis

Goal: compare symbol-bearing objects using consistent image and geometry methods.

Required for reproducibility:

- source images;
- preprocessing method;
- segmentation method;
- feature extraction method;
- similarity metric;
- clustering method;
- output matrix;
- interpretation boundary.

### 3. CP8 Operator Formalization

Goal: convert operator labels into defined functions or symbolic transformations.

Current labels:

```text
AFG
NSG
LRG
BFG
FCG
```

Each operator needs:

```text
name:
inputs:
outputs:
transform:
example:
test:
evidence_class:
```

### 4. Agent Cross-Verification

Goal: compare outputs from multiple agents without treating any single agent as final authority.

Research questions:

- Where do agents converge?
- Where do agents diverge?
- Which claims survive critique?
- Which claims need data?
- Which claims should remain symbolic?

### 5. HarmonyOS / Distributed Architecture Mapping

Goal: preserve and test the architectural analogy between HarmonyOS concepts and CP8 repository coordination.

---

## Research Evidence Rule

Every research result must state whether it is:

- an observation;
- an interpretation;
- a hypothesis;
- a local computation;
- an independently reviewed result;
- a reproducible result.

---

## Recommended Research Folder Template

```text
research/topic-name/
├── README.md
├── sources.md
├── raw/
├── processed/
├── scripts/
├── analysis/
├── visuals/
├── hashes.json
└── boundary.md
```
