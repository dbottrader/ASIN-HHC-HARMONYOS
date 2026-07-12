# ASIN Devices Recovery Specification v1.0

**Artifact family:** ASIN-HHC / CP8 / HarmonyOS  
**Recovered device chain:** Decode → Star Compass → Frequency Gate → Spiral Archive  
**Evidence class:** LOCAL reconstruction candidate  
**Date:** 2026-07-11

## Purpose

This specification reconstructs the lost ASIN crop-formation workflow as a deterministic software instrument.

The system converts a geometric profile into:

1. a canonical machine-readable record;
2. a deterministic byte and bit packet;
3. CP8 byte tokens;
4. synthetic control frequencies and phases;
5. Star Compass orientation values;
6. Frequency Gate filtered output;
7. a Spiral Archive visualization and export record.

## Claim boundary

The system is an experimental encoding and visualization instrument. It does not establish that crop formations contain literal machine code, extraterrestrial messages, or physically privileged frequencies.

A generated binary stream is a deterministic representation of the selected input fields and encoding rules. It is not proof that the original formation was designed as a binary transmission.

> No mechanism may silently convert uncertainty into authority.

## Input fields

- formation ID, title, location, year;
- source status: observed, reconstructed, or illustrative;
- rows and columns;
- node and ring counts;
- radial arms and symmetry order;
- rotation and center offsets;
- spiral direction;
- normalized size classes and ratios;
- optional literal source bitstream;
- measurement notes.

## Canonicalization

1. Unicode text is normalized conceptually to NFC.
2. Missing numeric fields become zero.
3. Object keys are sorted.
4. Arrays preserve their supplied order.
5. Runtime-only interface state is excluded.
6. Canonical JSON is serialized without insignificant whitespace.

## Packet

The implementation encodes:

- ASCII magic `ASIN`;
- schema version;
- source-status enumeration;
- year;
- rows and columns;
- node and ring counts;
- radial arms and symmetry order;
- rotation and center offsets;
- spiral direction;
- size classes and ratios;
- optional packed source bits;
- deterministic text digest;
- CRC-16/CCITT-FALSE.

## Star Compass

For direction count `D` and packet byte `b`:

```text
sector = b mod D
angle = sector × (360 / D)
```

The default direction count is the profile symmetry order, falling back to 12.

## Frequency mapping

The values `428`, `528`, and `963` are treated as protocol namespaces.

```text
normalized = byte / 255
frequency = namespace + normalized × span
phase = 2π × normalized
amplitude = 0.2 + 0.8 × normalized
```

## Frequency Gate

The gate applies a moving average followed by one of four deterministic rules:

- binary gate;
- low-pass threshold;
- high-pass threshold;
- band-pass window.

## Spiral Archive

```text
theta_i = i × golden_angle + phase_i
radius_i = scale × sqrt(i + 1)
```

Filtered packet events are rendered into a phyllotactic archive.

## Test profiles

- Chilbolton Arecibo-style 73 × 23 matrix reconstruction scaffold.
- Milk Hill six-arm, 409-node spiral reconstruction scaffold.

Both profiles are labeled reconstructed. Replace inferred values with measured source records before promoting them to source-grounded evidence.

## Promotion ladder

- **LOOM:** concept and symbolic interpretation.
- **LOCAL:** runnable deterministic implementation.
- **WITNESS:** reviewed by another person or system.
- **REPRO:** independently reproduced from sources and commands.
- **PRODUCTION:** deployed and operationally maintained.

**Fast exploration. Hard receipts. No fake authority.**
