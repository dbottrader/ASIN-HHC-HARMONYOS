# Evidence Classes

This repository can contain symbolic, creative, technical, experimental, and reproducible artifacts together. Evidence classes prevent category drift.

---

## LOOM

Symbolic, narrative, mythic, interpretive, visual, or poetic artifact.

Examples:

- crop/glyph reading pages;
- codex reflections;
- symbolic UI mockups;
- visual mythos diagrams;
- interpretive geometry notes.

Boundary:

`LOOM` artifacts do not claim scientific, engineering, clinical, hardware, cryptographic, legal, or production authority by default.

---

## LOCAL

Runnable, inspectable, or locally testable artifact.

Examples:

- one-file HTML UI;
- Python script;
- local JSON bundle;
- static web demo;
- local clustering notebook.

Boundary:

`LOCAL` means it runs or exists locally. It does not automatically mean externally verified.

---

## WITNESS

Artifact reviewed, checked, or critiqued by another agent, person, or process.

Examples:

- cross-agent critique;
- reviewer notes;
- witness handoff;
- structured audit report;
- promotion gate commentary.

Boundary:

`WITNESS` means reviewed, not necessarily reproduced.

---

## REPRO

Artifact with enough inputs, scripts, commands, and expected outputs to reproduce the result.

Examples:

- deterministic test harness;
- hash-verified bundle;
- Merkle build script;
- validation script with expected outputs;
- benchmark harness with baselines and ablations.

Boundary:

`REPRO` requires actual files and instructions, not just a report saying reproduction happened.

---

## PRODUCTION

Deployed and operationally maintained artifact.

Examples:

- deployed web app with monitoring;
- maintained API service;
- production automation pipeline;
- hardware/software system with operational tests.

Boundary:

`PRODUCTION` requires maintenance, monitoring, deployment notes, safety boundaries, and failure handling.

---

## Promotion Ladder

```text
LOOM -> LOCAL -> WITNESS -> REPRO -> PRODUCTION
```

Promotion should only happen when the required evidence is present in the repository or in a linked, stable, cited source.
