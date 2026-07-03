# HHC Lattice Operators

This file preserves the current operator vocabulary and glyph grammar notes for the ASIN-HHC / CP8 lattice layer.

---

## Known CP8 Operators

The following operator labels have appeared in the CP8 working system:

```text
AFG
NSG
LRG
BFG
FCG
```

These are preserved as symbolic/operator handles until each receives a formal definition, input/output contract, and test case.

---

## Known Glyph String

```text
⧖∞⧈✺⧉♓⟡⧗⟢✶◎◈ꗃ✦ᚾϞ⚯
```

Recommended treatment:

- Preserve as a glyph grammar seed.
- Do not treat as decoded binary unless a reproducible encoding method is attached.
- If vectorized, publish the vectorization method and feature schema.
- If clustered, publish source images, preprocessing, features, similarity metric, and clustering parameters.

---

## Suggested Formalization Schema

```json
{
  "glyph_id": "ANU-001",
  "symbol": "⧖",
  "name": "placeholder-name",
  "class": "axis/time/anchor/etc",
  "features": {
    "symmetry": null,
    "stroke_count": null,
    "radial_count": null,
    "intersection_count": null,
    "loop_count": null
  },
  "asin": {
    "anchor": null,
    "shape": null,
    "intention": null,
    "number": null
  },
  "evidence_class": "LOOM"
}
```

---

## Research Boundary

The glyph layer is valid as a symbolic grammar and design system. It becomes a technical model only when measurable features, reproducible transforms, and validation procedures are included.
