# ASIN-HHC / CP8 Provenance Rules

These rules define how project artifacts should be admitted, described, verified, and promoted.

---

## Rule 1 — Preserve Source Context

Every artifact should record where it came from, who generated it, and whether it was human-authored, AI-assisted, AI-generated, or mixed.

Minimum fields:

```text
title:
source:
author_or_agent:
date:
artifact_type:
evidence_class:
notes:
```

---

## Rule 2 — Separate Claim From Artifact

An artifact may be visually strong or symbolically meaningful without proving a technical or scientific claim.

Keep these separate:

- what the artifact is;
- what it appears to show;
- what it claims;
- what has actually been verified.

---

## Rule 3 — Hash Stable Artifacts

Stable files should receive a content hash when they become reference artifacts.

Recommended:

- SHA-256 for individual files.
- Merkle root for bundles.
- Import manifest for multi-file packages.

---

## Rule 4 — Record Promotion Boundary

Every promoted artifact should state what it is **not** claiming.

Example:

```text
This artifact is a symbolic interpretation and does not claim scientific, astronomical, clinical, hardware, or cryptographic authority.
```

---

## Rule 5 — Keep Raw and Derived Data Separate

Raw inputs, processed outputs, reports, visualizations, and summaries should live in separate paths.

Recommended:

```text
raw/
processed/
reports/
visuals/
manifests/
```

---

## Rule 6 — Reproduction Requires Instructions

A result is not reproducible unless another user can run the same procedure.

Minimum requirements:

- input files;
- command or script;
- dependency notes;
- expected output;
- expected hash or checksum when possible.

---

## Rule 7 — Agent Outputs Are Not Final Authority

AI agents can draft, critique, cluster, classify, summarize, and test. Their output should be marked as agent-generated unless independently verified.

---

## Rule 8 — Cascade Updates Must Be Traceable

A cascade import must include:

- branch name;
- date;
- purpose;
- changed files;
- evidence class;
- next required promotion step.

This prevents the archive from becoming a pile of files without lineage.
