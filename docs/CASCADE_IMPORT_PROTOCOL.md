# Cascade Import Protocol

Cascade is the controlled propagation of project data from scattered artifacts into a traceable repository lineage.

---

## 1. Purpose

The cascade protocol prevents the ASIN-HHC / CP8 archive from becoming a loose dump of files. Each important artifact should enter the repository with context, class, boundary, and next-step instructions.

---

## 2. Cascade Steps

1. **Receive artifact**  
   Identify source file, conversation, package, UI, script, report, image, JSON, or document.

2. **Name artifact**  
   Give it a stable, human-readable title.

3. **Classify artifact**  
   Assign evidence class: `LOOM`, `LOCAL`, `WITNESS`, `REPRO`, or `PRODUCTION`.

4. **Place artifact**  
   Store it in a meaningful path.

5. **Manifest artifact**  
   Add it to an index or JSON manifest.

6. **Hash artifact**  
   When stable, compute SHA-256 or bundle hash.

7. **Boundary artifact**  
   State what the artifact does and does not claim.

8. **Promote only with evidence**  
   Do not promote from symbolic to technical or technical to production without the necessary supporting files.

---

## 3. Import Branch Role

Branch: `project-import-20260703`

This branch is a staging branch for the important project data. It should receive curated documentation, manifests, UI artifacts, scripts, and provenance records before any merge into `main`.

---

## 4. Deep Research Expansion

For deep research, each topic should eventually receive:

```text
topic/
├── README.md
├── sources.md
├── raw/
├── processed/
├── analysis/
├── scripts/
├── visuals/
├── hashes.json
└── promotion-boundary.md
```

The archive should preserve both the creative symbolic layer and the hard verification layer, while never confusing one for the other.
