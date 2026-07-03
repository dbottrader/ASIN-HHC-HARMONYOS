# HarmonyOS Mapping for ASIN-HHC / CP8

This document preserves the working architecture analogy used across the ASIN-HHC / CP8 ecosystem.

---

## 1. Mapping Overview

| HarmonyOS Concept | CP8 / ASIN-HHC Equivalent | Function |
|---|---|---|
| Super Device | CP8 Lattice | Distributed artifacts behaving as one coordinated system |
| Soft Bus | Git + Issues + inbox/ + agent handoff | Message and artifact transport between nodes |
| Microkernel | Minimal trusted core | Smallest rule set that governs evidence, provenance, and execution |
| Manifest Topology | Explicit file maps and import manifests | Records what exists, where it lives, and how it connects |
| Deterministic Verification | Hashing, Merkle records, reproducible scripts | Confirms artifact integrity and lineage |
| Distributed Scheduling | Agent workflow / task routing | Moves work between human, AI agents, repos, and review stages |
| Device Trust | Evidence promotion gate | Separates symbolic, local, witness, reproducible, and production claims |

---

## 2. Seven Working Principles

1. **Everything has a manifest.** If an artifact matters, it needs a location, purpose, and status.
2. **Everything has a boundary.** Symbolic, experimental, local, witness, reproducible, and production artifacts must not be mixed without labels.
3. **Everything important gets hashed.** Hashes preserve identity across edits, bundles, and handoffs.
4. **Everything technical needs reproduction instructions.** A claim is stronger when another environment can reproduce the result.
5. **Everything symbolic remains valuable but properly scoped.** Mythic and visual material belongs in the archive, but it should not be promoted as scientific or engineering evidence without support.
6. **Everything agent-generated needs review.** Agent outputs are drafts or witnesses, not final authority by default.
7. **Everything converges through Git.** The repository becomes the anchor where scattered artifacts become a navigable lineage.

---

## 3. Recommended Repository Topology

```text
/
├── README.md
├── PROJECT_IMPORT_20260703.md
├── docs/
│   ├── CP8_ECOSYSTEM_MAP.md
│   ├── HARMONYOS_MAPPING.md
│   ├── PROVENANCE_RULES.md
│   ├── EVIDENCE_CLASSES.md
│   └── CASCADE_IMPORT_PROTOCOL.md
├── public/
│   ├── ui/
│   ├── codex/
│   └── visualizers/
├── hhc-lattice/
│   ├── glyphs.json
│   ├── operators.md
│   └── resonance-notes.md
├── manifests/
│   ├── artifact-index.json
│   ├── import-log.json
│   └── hashes.json
├── scripts/
│   ├── verify.py
│   ├── build-merkle.py
│   └── audit-packet.py
└── witness/
    ├── promotion-gate.md
    ├── critique-log.md
    └── handoff-template.md
```

---

## 4. Cascade Meaning

Within this project, **cascade** means controlled propagation:

1. A source artifact enters the archive.
2. It receives a manifest entry.
3. It receives an evidence class.
4. It is linked to supporting files.
5. It is optionally hashed.
6. It is optionally reviewed by another agent or human.
7. It can be promoted only when stronger evidence exists.

Cascade is therefore not just “upload everything.” It is structured convergence.
