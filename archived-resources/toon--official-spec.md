---
source_url: https://github.com/toon-format/spec
title: "TOON Official Specification (toon-format/spec)"
author: "Johann Schopplich"
publication_date: "2025-11-24 (v3.0)"
archive_date: "2026-05-17"
archived_by: "Claude Code (Opus 4.7)"
fetch_status: "ok"
---

# TOON Official Specification

**Source:** [github.com/toon-format/spec](https://github.com/toon-format/spec)
**Archived:** 2026-05-17
**Version:** 3.0 (Working Draft) - released 2025-11-24
**License:** MIT
**Media type (provisional):** `text/toon`

---

## Overview

> "TOON is a lossless serialization of the same objects, arrays, and primitives as JSON, but in a syntax that minimizes tokens and makes structure easy for models to follow."

Spec defines:

* Formal ABNF grammar
* 358+ test fixtures for cross-implementation validation
* Reference encoder/decoder in TypeScript

## How token savings are achieved

* Eliminates quotation marks on keys and most string values
* Eliminates `{` / `}` / `[` / `]` syntactic noise for simple objects/arrays (indentation does the work)
* Tabular arrays: single header `name[N]{field1,field2,...}:` followed by comma-separated rows, so field names appear once instead of per-element
* Length declarations `[N]` give the model an explicit count to validate against
* Implicit typing of unquoted scalars (numbers, booleans, null) via lexical rules

## Minimal example

JSON:

```json
{"name": "Blue Lake Trail", "distanceKm": 7.5, "companion": "ana"}
```

TOON:

```
name: Blue Lake Trail
distanceKm: 7.5
companion: ana
```

For uniform arrays of objects, header notation `hikes[3]{id,name,distanceKm}:` is followed by indented comma-separated rows.

## Status

Working Draft. No peer-reviewed academic validation yet (format publicly released October 2025). Reference TypeScript implementation maintained in the sibling `toon-format/toon` repo with 358+ conformance fixtures.
