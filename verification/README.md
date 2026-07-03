# Verification Plan

This directory is for reproducibility, hashing, audit packets, test instructions, and promotion evidence.

---

## Verification Goals

1. Preserve file identity with hashes.
2. Preserve bundle identity with Merkle-style manifests.
3. Separate symbolic artifacts from reproducible technical claims.
4. Provide commands and expected outputs for technical results.
5. Make future releases auditable.

---

## Verification Levels

### Level 0 — Preserved

Artifact exists in the repository.

### Level 1 — Has Metadata

Artifact has title, source, date, class, boundary, and path.

### Level 2 — Has Hash

Artifact has SHA-256 or bundle hash.

### Level 3 — Locally Runnable

Artifact can be run or inspected locally.

### Level 4 — Reproducible

Artifact includes source inputs, script, command, and expected output.

### Level 5 — Witnessed

Artifact has independent review or cross-agent critique.

### Level 6 — Release-Ready

Artifact is included in a versioned release with hashes and notes.

---

## Required Hash Format

```json
{
  "path": "relative/path/to/file",
  "sha256": "...",
  "bytes": 0,
  "date_hashed": "YYYY-MM-DD",
  "notes": ""
}
```

---

## Reproduction Record Template

```text
Title:
Artifact path:
Inputs:
Script/command:
Dependencies:
Expected output:
Expected hash:
Observed output:
Observed hash:
Result: PASS/FAIL
Reviewer:
Date:
```

---

## Standing Boundary

A verification file verifies only the property it measures. A file hash proves identity, not truth. A passing script proves local execution under stated conditions, not universal validity.
