# Coding Guidelines for mcp-alternatives Scripts

## Structure

Each script is **both** a CLI tool AND an importable module:

```python
#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml"]
# ///

def main_function():
    """Importable by other scripts."""
    pass

def main():
    """CLI entry point."""
    import argparse
    # ...

if __name__ == "__main__":
    main()
```

## Dependencies

- Use PEP 723 inline metadata for `uv run` compatibility
- Keep dependencies minimal: `pyyaml` required, `rich` optional for CLI output
- All scripts must work with Python 3.11+

## Conventions

### CLI Interface

- All scripts accept `--help`
- JSON output available via `--json` flag where applicable
- Paths relative to `mcp-alternatives/` directory

### Exit Codes

- `0` - Success
- `1` - General error
- `2` - Validation failure

### Output

- Default: Human-readable text
- `--json`: Machine-readable JSON
- `--quiet`: Suppress non-error output

## File Discovery

Scripts find data files relative to their location:

```python
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent  # mcp-alternatives/
REPO_ROOT = ROOT_DIR.parent   # repository root
```

## Testing

- Test scripts manually before committing
- Verify `--help` works
- Verify both CLI and import modes work

## Shared Code

Place shared utilities in `lib/`:

- `lib/loader.py` - YAML loading utilities
- `lib/renderer.py` - Markdown rendering utilities

Import with:

```python
from lib.loader import load_yaml_files
```
