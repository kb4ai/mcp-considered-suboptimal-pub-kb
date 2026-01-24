# MCP Alternatives Data-Driven System Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transform hand-maintained `mcp-alternatives.md` into a data-driven system with YAML sources, Python scripts, and GitHub issue templates.

**Architecture:** YAML data files at `mcp-alternatives/` root, static sections in `sections/`, Python scripts in `scripts/`, main regenerator at repo root. Convention-based ordering with numeric prefixes.

**Tech Stack:** Python 3.11+, PyYAML, uv for script execution, PEP 723 inline metadata.

---

## Phase 1: Directory Structure & Foundation

### Task 1.1: Create directory structure

**Files:**

- Create: `mcp-alternatives/` (directory)
- Create: `mcp-alternatives/spec/` (directory)
- Create: `mcp-alternatives/sections/` (directory)
- Create: `mcp-alternatives/scripts/` (directory)
- Create: `mcp-alternatives/scripts/lib/` (directory)

**Step 1: Create directories with .gitkeep files**

```bash
mkdir -p mcp-alternatives/spec
mkdir -p mcp-alternatives/sections
mkdir -p mcp-alternatives/scripts/lib
touch mcp-alternatives/spec/.gitkeep
touch mcp-alternatives/scripts/lib/.gitkeep
```

**Step 2: Commit**

```bash
git add mcp-alternatives/
git commit -m "Create mcp-alternatives directory structure"
```

---

### Task 1.2: Write CLI spec

**Files:**

- Create: `mcp-alternatives/spec/cli.spec.yaml`

**Step 1: Write the spec file**

```yaml
# Schema for CLI tool entries (*.cli.yaml)
# All fields optional except 'repo'

name: cli
description: CLI tool that replaces an MCP server
file_pattern: "*.cli.yaml"

required:
  - repo

fields:
  repo:
    type: string
    description: GitHub/GitLab URL or owner/repo shorthand
    examples:
      - "github.com/czottmann/linearis"
      - "cli/cli"

  name:
    type: string
    description: Display name (derived from repo if omitted)
    examples:
      - "Linearis"
      - "gh"

  service:
    type: string
    description: What service/API it interfaces with
    examples:
      - "Linear"
      - "GitHub"

  replaces_mcp:
    type: string
    description: Name of MCP server it replaces
    examples:
      - "Official Linear MCP"

  token_comparison:
    type: string
    description: Before/after token usage comparison
    examples:
      - "~13k → ~200"

  description:
    type: string
    description: Brief explanation of what it does

  quote:
    type: object
    description: Pull quote about the tool
    fields:
      text:
        type: string
        required: true
      source:
        type: string
        description: Author or article name
      url:
        type: string
        description: Link to source

  resources:
    type: list
    description: Related links (articles, gists, docs)
    items:
      type: object
      fields:
        label:
          type: string
          required: true
        url:
          type: string
          required: true
        archived:
          type: string
          description: Path to archived copy in archived-resources/

  author:
    type: string
    description: Tool author/maintainer

  tags:
    type: list
    items:
      type: string
    examples:
      - ["issue-tracking", "project-management"]
      - ["vcs", "code-review"]

  maturity:
    type: enum
    values: [alpha, beta, stable, unknown]
    default: unknown

  last_verified:
    type: date
    description: When we last confirmed it works (YYYY-MM-DD)
```

**Step 2: Commit**

```bash
git add mcp-alternatives/spec/cli.spec.yaml
git commit -m "Add CLI tool schema specification"
```

---

### Task 1.3: Write wanted spec

**Files:**

- Create: `mcp-alternatives/spec/wanted.spec.yaml`

**Step 1: Write the spec file**

```yaml
# Schema for wanted entries (*.wanted.yaml)
# All fields optional - low barrier for contributions

name: wanted
description: Request for a CLI alternative to an MCP server
file_pattern: "*.wanted.yaml"

required: []

fields:
  service:
    type: string
    description: Service name
    examples:
      - "Notion"
      - "Jira"

  mcp_exists:
    type: boolean
    description: Is there an MCP server for this service?
    default: true

  existing_clis:
    type: list
    description: Known CLI tools that might work (unverified)
    items:
      type: string
    examples:
      - ["jira-cli", "go-jira"]

  pain_points:
    type: string
    description: What's wrong with current options

  requested_by:
    type: string
    description: GitHub username or "anonymous"
```

**Step 2: Commit**

```bash
git add mcp-alternatives/spec/wanted.spec.yaml
git commit -m "Add wanted entry schema specification"
```

---

### Task 1.4: Write CODING_GUIDELINES.md

**Files:**

- Create: `mcp-alternatives/scripts/CODING_GUIDELINES.md`

**Step 1: Write the guidelines**

```markdown
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
```

**Step 2: Commit**

```bash
git add mcp-alternatives/scripts/CODING_GUIDELINES.md
git commit -m "Add coding guidelines for mcp-alternatives scripts"
```

---

## Phase 2: Data Migration

### Task 2.1: Create Linearis CLI entry

**Files:**

- Create: `mcp-alternatives/linearis.cli.yaml`

**Step 1: Write the YAML file**

```yaml
repo: github.com/czottmann/linearis
name: Linearis
service: Linear
replaces_mcp: Official Linear MCP
token_comparison: "~13k → ~200"
description: CLI tool for Linear issue tracking, built for LLM agents
author: Carlo Zottmann

quote:
  text: "Token budget matters: 13k tokens for tool definitions is prohibitive. Simplicity wins: 3-4 features beats 20+ for real workflows."
  source: Carlo Zottmann
  url: https://zottmann.org/2025/09/03/linearis-my-linear-cli-built.html

resources:
  - label: GitHub Repository
    url: https://github.com/czottmann/linearis
  - label: Design Article
    url: https://zottmann.org/2025/09/03/linearis-my-linear-cli-built.html
    archived: archived-resources/zottmann--linearis-linear-cli-built.md
  - label: Workarounds & Extensions
    url: https://gist.github.com/g-click-trade/3d73f0492abd2e5c75baa863053867dc

tags:
  - issue-tracking
  - project-management

maturity: stable
```

**Step 2: Commit**

```bash
git add mcp-alternatives/linearis.cli.yaml
git commit -m "Add Linearis CLI tool entry"
```

---

### Task 2.2: Create gh CLI entry

**Files:**

- Create: `mcp-alternatives/gh.cli.yaml`

**Step 1: Write the YAML file**

```yaml
repo: github.com/cli/cli
name: gh
service: GitHub
replaces_mcp: GitHub MCP servers
description: Official GitHub CLI - pre-trained in LLMs, fully scriptable

resources:
  - label: GitHub Repository
    url: https://github.com/cli/cli
  - label: Documentation
    url: https://cli.github.com/manual/

tags:
  - vcs
  - code-review
  - issues
  - pull-requests

maturity: stable

examples:
  - command: "gh issue list --limit 20 --json title,number | jq '.[].title'"
    description: List issue titles
  - command: "gh pr view 123 --json body,reviews"
    description: View PR details
  - command: "gh api repos/owner/repo/commits --paginate | jq '.[].sha'"
    description: List commit SHAs
```

**Step 2: Commit**

```bash
git add mcp-alternatives/gh.cli.yaml
git commit -m "Add gh (GitHub CLI) tool entry"
```

---

### Task 2.3: Create slack-cli-mcp-wrapper entry

**Files:**

- Create: `mcp-alternatives/slack-cli-mcp-wrapper.cli.yaml`

**Step 1: Write the YAML file**

```yaml
repo: github.com/CLIAI/slack-cli-mcp-wrapper
name: slack-cli-mcp-wrapper
service: Slack
replaces_mcp: Official Slack MCP
description: CLI wrapper providing Slack access that agents can script, filter, and audit

tags:
  - chat
  - messaging

maturity: unknown
```

**Step 2: Commit**

```bash
git add mcp-alternatives/slack-cli-mcp-wrapper.cli.yaml
git commit -m "Add slack-cli-mcp-wrapper entry"
```

---

### Task 2.4: Create wanted entries

**Files:**

- Create: `mcp-alternatives/jira.wanted.yaml`
- Create: `mcp-alternatives/notion.wanted.yaml`
- Create: `mcp-alternatives/confluence.wanted.yaml`
- Create: `mcp-alternatives/google-drive.wanted.yaml`
- Create: `mcp-alternatives/figma.wanted.yaml`
- Create: `mcp-alternatives/asana.wanted.yaml`

**Step 1: Write jira.wanted.yaml**

```yaml
service: Jira
mcp_exists: true
existing_clis:
  - jira-cli
pain_points: Need verification if existing CLIs work well with LLM agents
```

**Step 2: Write notion.wanted.yaml**

```yaml
service: Notion
mcp_exists: true
existing_clis: []
pain_points: No known agent-friendly CLI alternative
```

**Step 3: Write confluence.wanted.yaml**

```yaml
service: Confluence
mcp_exists: true
existing_clis: []
```

**Step 4: Write google-drive.wanted.yaml**

```yaml
service: Google Drive
mcp_exists: true
existing_clis:
  - gdrive
  - rclone
pain_points: Need verification if existing CLIs work well with LLM agents
```

**Step 5: Write figma.wanted.yaml**

```yaml
service: Figma
mcp_exists: true
existing_clis: []
```

**Step 6: Write asana.wanted.yaml**

```yaml
service: Asana
mcp_exists: true
existing_clis: []
```

**Step 7: Commit**

```bash
git add mcp-alternatives/*.wanted.yaml
git commit -m "Add wanted entries for services needing CLI alternatives"
```

---

## Phase 3: Static Sections

### Task 3.1: Create intro section

**Files:**

- Create: `mcp-alternatives/sections/00-intro.section.md`

**Step 1: Write the section**

```markdown
# MCP Alternatives: CLI Tools for LLM Agents

*CLI tools that replace MCP servers — scriptable, auditable, token-efficient.*

---
```

**Step 2: Commit**

```bash
git add mcp-alternatives/sections/00-intro.section.md
git commit -m "Add intro section"
```

---

### Task 3.2: Create why-cli section

**Files:**

- Create: `mcp-alternatives/sections/10-why-cli.section.md`

**Step 1: Write the section**

```markdown
## Why CLI Over MCP?

| Benefit | How CLI Delivers |
|---------|------------------|
| **Token efficiency** | No upfront tool definitions (~13k → ~200 tokens) |
| **Scriptability** | Chain commands, loops, conditionals |
| **Fuzzy search** | Filter results with `sk -f`, `fzf`, `rg` before context |
| **Audit logs** | Wrap CLI calls with logging, validation |
| **Composability** | Pipe JSON through `jq`, combine tools freely |

---
```

**Step 2: Commit**

```bash
git add mcp-alternatives/sections/10-why-cli.section.md
git commit -m "Add why-cli section"
```

---

### Task 3.3: Create generated markers

**Files:**

- Create: `mcp-alternatives/sections/20-cli-tools.generated`
- Create: `mcp-alternatives/sections/30-wanted.generated`

**Step 1: Write cli-tools marker**

```
# GENERATED: CLI Tools
# This marker tells the regenerate script to insert CLI tool entries here.
# Do not edit - content is generated from *.cli.yaml files.
type: cli
heading: "## Alternatives by Service"
```

**Step 2: Write wanted marker**

```
# GENERATED: Wanted
# This marker tells the regenerate script to insert wanted entries here.
# Do not edit - content is generated from *.wanted.yaml files.
type: wanted
heading: "## More Services (Help Wanted)"
```

**Step 3: Commit**

```bash
git add mcp-alternatives/sections/*.generated
git commit -m "Add generated section markers"
```

---

### Task 3.4: Create patterns section

**Files:**

- Create: `mcp-alternatives/sections/80-patterns.section.md`

**Step 1: Write the section**

```markdown
## Design Patterns for Agent-Friendly CLIs

When building or choosing CLI tools for LLM agents:

1. **`usage` or `--help` command** — Self-documenting for agents
2. **JSON output** — Composable with `jq`, `yq`
3. **Focused scope** — 3-5 core operations, not 20+
4. **Smart ID resolution** — Accept natural formats (e.g., `ABC-123`)
5. **Exit codes** — Clear success/failure for scripting
6. **Streaming support** — Don't buffer huge responses

See [CLI/SDK Over Context Bloat](cli-sdk-over-context-bloat.md) for detailed patterns.

---
```

**Step 2: Commit**

```bash
git add mcp-alternatives/sections/80-patterns.section.md
git commit -m "Add design patterns section"
```

---

### Task 3.5: Create contribute section

**Files:**

- Create: `mcp-alternatives/sections/90-contribute.section.md`

**Step 1: Write the section**

```markdown
## Contribute: Share Your CLI Tools

**We want to hear from you!**

### Ways to Contribute

| Method | Best For |
|--------|----------|
| [Submit CLI Tool](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/issues/new?template=submit-cli-tool.md) | Share a CLI alternative you've found or built |
| [Request Alternative](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/issues/new?template=request-alternative.md) | Ask for a CLI replacement for an MCP server |
| [Suggest Edit](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/issues/new?template=suggest-edit.md) | Typos, corrections, improvements |
| [Add Resource](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/issues/new?template=add-resource.md) | Share quotes, articles, sources |
| [Pull Request](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/pulls) | Direct contributions (preferred!) |

### For Contributors

Data lives in `mcp-alternatives/` directory:

- `*.cli.yaml` — CLI tool entries
- `*.wanted.yaml` — Wanted entries
- Run `./mcp-alternatives.regenerate.py` to rebuild the document

See [`mcp-alternatives/AGENTS.md`](mcp-alternatives/AGENTS.md) for schema details.

---

## Further Reading

* [Core Thesis](THESIS.md) — Why CLI beats MCP
* [FAQ](FAQ.md) — Sandboxing, lazy loading, self-optimization
* [MCP Critique Sources](mcp-critique-sources.md) — Industry voices

---

*Part of [MCP Considered Suboptimal](https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb)*
```

**Step 2: Commit**

```bash
git add mcp-alternatives/sections/90-contribute.section.md
git commit -m "Add contribute section with issue template links"
```

---

## Phase 4: Core Scripts

### Task 4.1: Create shared loader library

**Files:**

- Create: `mcp-alternatives/scripts/lib/loader.py`

**Step 1: Write the loader**

```python
#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml"]
# ///
"""Shared utilities for loading YAML data files."""

from pathlib import Path
from typing import Any
import yaml

SCRIPT_DIR = Path(__file__).parent
ROOT_DIR = SCRIPT_DIR.parent.parent  # mcp-alternatives/


def get_root_dir() -> Path:
    """Return the mcp-alternatives directory."""
    return ROOT_DIR


def load_yaml(path: Path) -> dict[str, Any]:
    """Load a single YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_yaml_files(pattern: str) -> list[tuple[Path, dict[str, Any]]]:
    """Load all YAML files matching pattern from root directory.

    Returns list of (path, data) tuples.
    """
    results = []
    for path in sorted(ROOT_DIR.glob(pattern)):
        if path.is_file():
            try:
                data = load_yaml(path)
                results.append((path, data))
            except yaml.YAMLError as e:
                print(f"Warning: Failed to parse {path}: {e}")
    return results


def load_cli_entries() -> list[tuple[Path, dict[str, Any]]]:
    """Load all CLI tool entries."""
    return load_yaml_files("*.cli.yaml")


def load_wanted_entries() -> list[tuple[Path, dict[str, Any]]]:
    """Load all wanted entries."""
    return load_yaml_files("*.wanted.yaml")


def load_spec(spec_type: str) -> dict[str, Any]:
    """Load a spec file by type (cli, wanted)."""
    spec_path = ROOT_DIR / "spec" / f"{spec_type}.spec.yaml"
    if spec_path.exists():
        return load_yaml(spec_path)
    return {}


if __name__ == "__main__":
    # Quick test
    print("CLI entries:", len(load_cli_entries()))
    print("Wanted entries:", len(load_wanted_entries()))
```

**Step 2: Remove .gitkeep and commit**

```bash
rm mcp-alternatives/scripts/lib/.gitkeep
git add mcp-alternatives/scripts/lib/loader.py
git commit -m "Add shared YAML loader library"
```

---

### Task 4.2: Create validate script

**Files:**

- Create: `mcp-alternatives/scripts/validate.py`

**Step 1: Write the validator**

```python
#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml"]
# ///
"""Validate YAML data files against their specs."""

import argparse
import sys
from pathlib import Path
from typing import Any

# Add lib to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from lib.loader import load_yaml, load_cli_entries, load_wanted_entries, load_spec, get_root_dir


def validate_entry(data: dict[str, Any], spec: dict[str, Any], path: Path) -> list[str]:
    """Validate a single entry against its spec. Returns list of errors."""
    errors = []

    # Check required fields
    for field in spec.get("required", []):
        if field not in data or data[field] is None or data[field] == "":
            errors.append(f"{path.name}: Missing required field '{field}'")

    # Check field types (basic validation)
    fields_spec = spec.get("fields", {})
    for field, value in data.items():
        if field not in fields_spec:
            continue  # Allow extra fields

        field_spec = fields_spec[field]
        expected_type = field_spec.get("type")

        if expected_type == "string" and not isinstance(value, str):
            errors.append(f"{path.name}: Field '{field}' should be string, got {type(value).__name__}")
        elif expected_type == "boolean" and not isinstance(value, bool):
            errors.append(f"{path.name}: Field '{field}' should be boolean, got {type(value).__name__}")
        elif expected_type == "list" and not isinstance(value, list):
            errors.append(f"{path.name}: Field '{field}' should be list, got {type(value).__name__}")
        elif expected_type == "object" and not isinstance(value, dict):
            errors.append(f"{path.name}: Field '{field}' should be object, got {type(value).__name__}")
        elif expected_type == "enum":
            valid_values = field_spec.get("values", [])
            if value not in valid_values:
                errors.append(f"{path.name}: Field '{field}' must be one of {valid_values}, got '{value}'")

    return errors


def validate_all(strict: bool = False) -> tuple[bool, list[str]]:
    """Validate all entries. Returns (success, errors)."""
    all_errors = []

    # Load specs
    cli_spec = load_spec("cli")
    wanted_spec = load_spec("wanted")

    # Validate CLI entries
    for path, data in load_cli_entries():
        errors = validate_entry(data, cli_spec, path)
        all_errors.extend(errors)

    # Validate wanted entries
    for path, data in load_wanted_entries():
        errors = validate_entry(data, wanted_spec, path)
        all_errors.extend(errors)

    success = len(all_errors) == 0
    return success, all_errors


def main():
    parser = argparse.ArgumentParser(description="Validate YAML data files")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    success, errors = validate_all(strict=args.strict)

    if args.json:
        import json
        print(json.dumps({"success": success, "errors": errors}))
    else:
        if errors:
            print("Validation errors:")
            for error in errors:
                print(f"  - {error}")
        else:
            print("All files valid.")

    sys.exit(0 if success else 2)


if __name__ == "__main__":
    main()
```

**Step 2: Make executable and commit**

```bash
chmod +x mcp-alternatives/scripts/validate.py
git add mcp-alternatives/scripts/validate.py
git commit -m "Add validation script for YAML entries"
```

---

### Task 4.3: Create table renderer

**Files:**

- Create: `mcp-alternatives/scripts/lib/renderer.py`

**Step 1: Write the renderer**

```python
#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml"]
# ///
"""Markdown rendering utilities."""

from pathlib import Path
from typing import Any


def render_cli_entry(data: dict[str, Any]) -> str:
    """Render a single CLI entry as markdown."""
    lines = []

    # Header with service name
    service = data.get("service", "Unknown Service")
    lines.append(f"### {service}")
    lines.append("")

    # Comparison table
    name = data.get("name", data.get("repo", "").split("/")[-1])
    repo = data.get("repo", "")
    replaces = data.get("replaces_mcp", "MCP Server")
    token_comp = data.get("token_comparison", "")

    # Build repo link
    if repo:
        if not repo.startswith("http"):
            repo_url = f"https://{repo}"
        else:
            repo_url = repo
        name_link = f"[{name}]({repo_url})"
    else:
        name_link = name

    lines.append("| MCP Server | CLI Alternative |")
    lines.append("|------------|-----------------|")

    if token_comp:
        lines.append(f"| {replaces} ({token_comp.split('→')[0].strip()}) | {name_link} ({token_comp.split('→')[-1].strip()}) |")
    else:
        lines.append(f"| {replaces} | {name_link} |")

    # Description
    if data.get("description"):
        lines.append("")
        lines.append(data["description"])

    # Resources
    resources = data.get("resources", [])
    if resources:
        lines.append("")
        lines.append("**Resources:**")
        lines.append("")
        for res in resources:
            label = res.get("label", "Link")
            url = res.get("url", "")
            archived = res.get("archived", "")
            if archived:
                lines.append(f"* [{label}]({url}) ([archived]({archived}))")
            else:
                lines.append(f"* [{label}]({url})")

    # Quote
    quote = data.get("quote")
    if quote:
        lines.append("")
        lines.append("**Why it wins:**")
        lines.append("")
        lines.append(f"> \"{quote.get('text', '')}\"")
        if quote.get("source"):
            lines.append(f"> — {quote['source']}")

    # Examples
    examples = data.get("examples", [])
    if examples:
        lines.append("")
        lines.append("**Examples:**")
        lines.append("")
        lines.append("```bash")
        for ex in examples:
            if ex.get("description"):
                lines.append(f"# {ex['description']}")
            lines.append(ex.get("command", ""))
        lines.append("```")

    lines.append("")
    lines.append("---")

    return "\n".join(lines)


def render_cli_entries(entries: list[tuple[Path, dict[str, Any]]]) -> str:
    """Render all CLI entries as markdown."""
    if not entries:
        return "*No CLI alternatives documented yet.*"

    parts = []
    for path, data in entries:
        parts.append(render_cli_entry(data))

    return "\n\n".join(parts)


def render_wanted_table(entries: list[tuple[Path, dict[str, Any]]]) -> str:
    """Render wanted entries as a table."""
    if not entries:
        return "*No requests yet.*"

    lines = []
    lines.append("We're tracking CLI alternatives for common MCP servers. See \"Contribute\" below.")
    lines.append("")
    lines.append("| Service | MCP Server Exists? | CLI Alternative? |")
    lines.append("|---------|-------------------|------------------|")

    for path, data in entries:
        service = data.get("service", path.stem)
        mcp_exists = "Yes" if data.get("mcp_exists", True) else "No"
        existing = data.get("existing_clis", [])
        if existing:
            cli_alt = ", ".join(f"`{c}`?" for c in existing)
        else:
            cli_alt = "?"

        lines.append(f"| {service} | {mcp_exists} | {cli_alt} |")

    lines.append("")
    lines.append("---")

    return "\n".join(lines)


if __name__ == "__main__":
    # Quick test
    print("Renderer module loaded successfully")
```

**Step 2: Commit**

```bash
git add mcp-alternatives/scripts/lib/renderer.py
git commit -m "Add markdown rendering library"
```

---

### Task 4.4: Create regenerate script

**Files:**

- Create: `mcp-alternatives.regenerate.py`

**Step 1: Write the regenerator**

```python
#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml"]
# ///
"""Regenerate mcp-alternatives.md from YAML data and section files."""

import argparse
import sys
from pathlib import Path

# Add scripts to path
REPO_ROOT = Path(__file__).parent
MCP_ALT_DIR = REPO_ROOT / "mcp-alternatives"
SCRIPTS_DIR = MCP_ALT_DIR / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from lib.loader import load_cli_entries, load_wanted_entries
from lib.renderer import render_cli_entries, render_wanted_table
from validate import validate_all


def load_sections() -> list[tuple[str, str, str]]:
    """Load section files in order.

    Returns list of (filename, type, content) tuples.
    Type is 'static' for .section.md files, or the type from .generated files.
    """
    sections_dir = MCP_ALT_DIR / "sections"
    sections = []

    for path in sorted(sections_dir.glob("*")):
        if path.suffix == ".md" and ".section" in path.name:
            # Static section
            content = path.read_text(encoding="utf-8")
            sections.append((path.name, "static", content))
        elif path.name.endswith(".generated"):
            # Generated section - parse the marker
            content = path.read_text(encoding="utf-8")
            # Extract type from marker
            gen_type = "unknown"
            heading = ""
            for line in content.split("\n"):
                if line.startswith("type:"):
                    gen_type = line.split(":", 1)[1].strip()
                elif line.startswith("heading:"):
                    heading = line.split(":", 1)[1].strip().strip('"')
            sections.append((path.name, gen_type, heading))

    return sections


def generate_content(gen_type: str, heading: str) -> str:
    """Generate content for a generated section."""
    lines = []

    if heading:
        lines.append(heading)
        lines.append("")

    if gen_type == "cli":
        entries = load_cli_entries()
        lines.append(render_cli_entries(entries))
    elif gen_type == "wanted":
        entries = load_wanted_entries()
        lines.append(render_wanted_table(entries))
    else:
        lines.append(f"*Unknown generator type: {gen_type}*")

    return "\n".join(lines)


def regenerate(validate_first: bool = True, dry_run: bool = False) -> bool:
    """Regenerate mcp-alternatives.md.

    Returns True on success, False on failure.
    """
    # Validate first
    if validate_first:
        success, errors = validate_all()
        if not success:
            print("Validation failed:")
            for error in errors:
                print(f"  - {error}")
            return False

    # Load sections
    sections = load_sections()

    # Build output
    output_parts = []
    for filename, sec_type, content in sections:
        if sec_type == "static":
            output_parts.append(content.rstrip())
        else:
            generated = generate_content(sec_type, content)
            output_parts.append(generated.rstrip())

    output = "\n\n".join(output_parts) + "\n"

    # Write output
    output_path = REPO_ROOT / "mcp-alternatives.md"

    if dry_run:
        print("=== DRY RUN - Would write to mcp-alternatives.md ===")
        print(output)
        return True

    output_path.write_text(output, encoding="utf-8")
    print(f"Regenerated {output_path}")
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Regenerate mcp-alternatives.md from YAML data"
    )
    parser.add_argument(
        "--no-validate",
        action="store_true",
        help="Skip validation before regenerating"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print output instead of writing to file"
    )
    args = parser.parse_args()

    success = regenerate(
        validate_first=not args.no_validate,
        dry_run=args.dry_run
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
```

**Step 2: Make executable and commit**

```bash
chmod +x mcp-alternatives.regenerate.py
git add mcp-alternatives.regenerate.py
git commit -m "Add main regeneration script"
```

---

### Task 4.5: Test regeneration

**Step 1: Run regeneration**

```bash
./mcp-alternatives.regenerate.py
```

Expected: Success message, regenerated file.

**Step 2: Verify output**

```bash
head -50 mcp-alternatives.md
```

**Step 3: Run with dry-run to inspect**

```bash
./mcp-alternatives.regenerate.py --dry-run | head -100
```

**Step 4: Commit regenerated file**

```bash
git add mcp-alternatives.md
git commit -m "Regenerate mcp-alternatives.md from data files"
```

---

## Phase 5: Additional Scripts

### Task 5.1: Create query script

**Files:**

- Create: `mcp-alternatives/scripts/query.py`

**Step 1: Write the script**

```python
#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml"]
# ///
"""Query and filter YAML data entries."""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))
from lib.loader import load_cli_entries, load_wanted_entries


def query(
    entry_type: str = "all",
    service: str | None = None,
    has_field: str | None = None,
    tag: str | None = None,
) -> list[dict[str, Any]]:
    """Query entries with filters.

    Args:
        entry_type: "cli", "wanted", or "all"
        service: Filter by service name (case-insensitive substring)
        has_field: Only entries that have this field set
        tag: Filter by tag (cli entries only)

    Returns:
        List of matching entries with metadata.
    """
    results = []

    # Load entries
    if entry_type in ("cli", "all"):
        for path, data in load_cli_entries():
            entry = {"_type": "cli", "_file": path.name, **data}
            results.append(entry)

    if entry_type in ("wanted", "all"):
        for path, data in load_wanted_entries():
            entry = {"_type": "wanted", "_file": path.name, **data}
            results.append(entry)

    # Apply filters
    if service:
        service_lower = service.lower()
        results = [
            e for e in results
            if service_lower in e.get("service", "").lower()
        ]

    if has_field:
        results = [
            e for e in results
            if has_field in e and e[has_field] is not None and e[has_field] != ""
        ]

    if tag:
        tag_lower = tag.lower()
        results = [
            e for e in results
            if tag_lower in [t.lower() for t in e.get("tags", [])]
        ]

    return results


def main():
    parser = argparse.ArgumentParser(description="Query YAML data entries")
    parser.add_argument(
        "--type",
        choices=["cli", "wanted", "all"],
        default="all",
        help="Entry type to query"
    )
    parser.add_argument("--service", help="Filter by service name")
    parser.add_argument("--has", dest="has_field", help="Filter by field presence")
    parser.add_argument("--tag", help="Filter by tag")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    results = query(
        entry_type=args.type,
        service=args.service,
        has_field=args.has_field,
        tag=args.tag,
    )

    if args.json:
        print(json.dumps(results, indent=2, default=str))
    else:
        if not results:
            print("No matching entries.")
        else:
            for entry in results:
                print(f"[{entry['_type']}] {entry['_file']}")
                if entry.get("service"):
                    print(f"  Service: {entry['service']}")
                if entry.get("name"):
                    print(f"  Name: {entry['name']}")
                if entry.get("repo"):
                    print(f"  Repo: {entry['repo']}")
                print()

    sys.exit(0)


if __name__ == "__main__":
    main()
```

**Step 2: Make executable and commit**

```bash
chmod +x mcp-alternatives/scripts/query.py
git add mcp-alternatives/scripts/query.py
git commit -m "Add query script for filtering entries"
```

---

### Task 5.2: Create stats script

**Files:**

- Create: `mcp-alternatives/scripts/stats.py`

**Step 1: Write the script**

```python
#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml"]
# ///
"""Generate statistics about the data."""

import argparse
import json
import sys
from pathlib import Path
from collections import Counter

sys.path.insert(0, str(Path(__file__).parent))
from lib.loader import load_cli_entries, load_wanted_entries


def get_stats() -> dict:
    """Compute statistics about the data."""
    cli_entries = load_cli_entries()
    wanted_entries = load_wanted_entries()

    stats = {
        "cli_count": len(cli_entries),
        "wanted_count": len(wanted_entries),
        "total_count": len(cli_entries) + len(wanted_entries),
    }

    # CLI completeness
    cli_fields = ["name", "service", "description", "quote", "resources", "tags"]
    completeness = Counter()
    for path, data in cli_entries:
        for field in cli_fields:
            if field in data and data[field]:
                completeness[field] += 1

    stats["cli_completeness"] = {
        field: f"{completeness[field]}/{len(cli_entries)}"
        for field in cli_fields
    }

    # Tags distribution
    all_tags = []
    for path, data in cli_entries:
        all_tags.extend(data.get("tags", []))
    stats["tag_counts"] = dict(Counter(all_tags))

    # Services covered
    services = set()
    for path, data in cli_entries:
        if data.get("service"):
            services.add(data["service"])
    stats["services_with_cli"] = sorted(services)

    # Services wanted
    wanted_services = set()
    for path, data in wanted_entries:
        if data.get("service"):
            wanted_services.add(data["service"])
    stats["services_wanted"] = sorted(wanted_services)

    return stats


def main():
    parser = argparse.ArgumentParser(description="Show data statistics")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    stats = get_stats()

    if args.json:
        print(json.dumps(stats, indent=2))
    else:
        print("=== MCP Alternatives Statistics ===")
        print()
        print(f"CLI tools documented: {stats['cli_count']}")
        print(f"Wanted entries: {stats['wanted_count']}")
        print()
        print("CLI field completeness:")
        for field, count in stats["cli_completeness"].items():
            print(f"  {field}: {count}")
        print()
        print(f"Services with CLI alternatives: {', '.join(stats['services_with_cli'])}")
        print(f"Services wanted: {', '.join(stats['services_wanted'])}")
        if stats["tag_counts"]:
            print()
            print("Tags:")
            for tag, count in sorted(stats["tag_counts"].items()):
                print(f"  {tag}: {count}")

    sys.exit(0)


if __name__ == "__main__":
    main()
```

**Step 2: Make executable and commit**

```bash
chmod +x mcp-alternatives/scripts/stats.py
git add mcp-alternatives/scripts/stats.py
git commit -m "Add statistics script"
```

---

## Phase 6: AGENTS.md

### Task 6.1: Create AGENTS.md

**Files:**

- Create: `mcp-alternatives/AGENTS.md`

**Step 1: Write the file**

```markdown
# MCP Alternatives: Agent Guide

Quick reference for LLM agents working with this directory.

## Directory Layout

```
mcp-alternatives/
├── *.cli.yaml          # CLI tool entries (source of truth)
├── *.wanted.yaml       # Wanted entries (help needed)
├── spec/               # YAML schemas
├── sections/           # Static markdown sections
└── scripts/            # Python utilities
```

## Adding a CLI Tool

Create `{name}.cli.yaml`:

```yaml
repo: github.com/owner/repo      # Required
name: Tool Name                   # Optional (derived from repo)
service: ServiceName              # What it replaces
replaces_mcp: MCP Server Name     # Optional
token_comparison: "~13k → ~200"   # Optional
description: Brief explanation    # Optional
tags: [category1, category2]      # Optional
maturity: stable                  # alpha/beta/stable/unknown
```

## Adding a Wanted Entry

Create `{service}.wanted.yaml`:

```yaml
service: ServiceName
mcp_exists: true
existing_clis: [cli1, cli2]      # Unverified options
pain_points: What's wrong
```

## Scripts

All scripts support `--help` and `--json` output.

```bash
# Validate all entries
./mcp-alternatives/scripts/validate.py

# Query entries
./mcp-alternatives/scripts/query.py --service=Linear
./mcp-alternatives/scripts/query.py --type=cli --has=quote

# Show statistics
./mcp-alternatives/scripts/stats.py

# Regenerate the document
./mcp-alternatives.regenerate.py
```

## Regeneration

After modifying YAML files, run:

```bash
./mcp-alternatives.regenerate.py
```

This validates entries and rebuilds `mcp-alternatives.md`.

## Schemas

Full schemas in `spec/cli.spec.yaml` and `spec/wanted.spec.yaml`.

Key rules:
- CLI entries require `repo` field
- Wanted entries have no required fields
- All other fields optional (low contribution barrier)
```

**Step 2: Commit**

```bash
git add mcp-alternatives/AGENTS.md
git commit -m "Add AGENTS.md for LLM agent guidance"
```

---

## Phase 7: GitHub Issue Templates

### Task 7.1: Create issue template config

**Files:**

- Create: `.github/ISSUE_TEMPLATE/config.yml`

**Step 1: Create directory and config**

```bash
mkdir -p .github/ISSUE_TEMPLATE
```

```yaml
blank_issues_enabled: true
contact_links:
  - name: Pull Request
    url: https://github.com/kb4ai/mcp-considered-suboptimal-pub-kb/pulls
    about: Prefer PRs for direct contributions to data files
```

**Step 2: Commit**

```bash
git add .github/ISSUE_TEMPLATE/config.yml
git commit -m "Add GitHub issue template config"
```

---

### Task 7.2: Create submit-cli-tool template

**Files:**

- Create: `.github/ISSUE_TEMPLATE/submit-cli-tool.md`

**Step 1: Write the template**

````markdown
---
name: Submit CLI Tool
about: Share a CLI alternative to an MCP server
title: "[CLI] "
labels: cli-tool, contribution
---

**Copy and fill the YAML below** (all fields optional except repo):

```yaml
repo:
name:
service:
replaces_mcp:
token_comparison:
description:
author:
tags: []
maturity:  # alpha, beta, stable, unknown

quote:
  text:
  source:
  url:

resources:
  - label:
    url:
```

**Why does this tool work well for LLM agents?**

<!-- Examples: JSON output, good --help, focused scope, scriptable -->

**Anything else?**
````

**Step 2: Commit**

```bash
git add .github/ISSUE_TEMPLATE/submit-cli-tool.md
git commit -m "Add issue template for CLI tool submissions"
```

---

### Task 7.3: Create request-alternative template

**Files:**

- Create: `.github/ISSUE_TEMPLATE/request-alternative.md`

**Step 1: Write the template**

````markdown
---
name: Request CLI Alternative
about: Request a CLI replacement for an MCP server
title: "[Wanted] "
labels: wanted, help-wanted
---

**What service needs a CLI alternative?**

```yaml
service:
mcp_exists: true
existing_clis: []
pain_points:
```

**What would make a good CLI for this service?**

<!-- What features would be most useful? -->

**Have you tried any existing tools?**

<!-- If so, what was your experience? -->
````

**Step 2: Commit**

```bash
git add .github/ISSUE_TEMPLATE/request-alternative.md
git commit -m "Add issue template for CLI alternative requests"
```

---

### Task 7.4: Create suggest-edit template

**Files:**

- Create: `.github/ISSUE_TEMPLATE/suggest-edit.md`

**Step 1: Write the template**

```markdown
---
name: Suggest Edit
about: Typos, rewording, corrections, errata
title: "[Edit] "
labels: documentation
---

**What needs fixing?**

**Where?** (file path or section name)

**Current text:**

**Suggested text:**

**Why this change?**
```

**Step 2: Commit**

```bash
git add .github/ISSUE_TEMPLATE/suggest-edit.md
git commit -m "Add issue template for edit suggestions"
```

---

### Task 7.5: Create add-resource template

**Files:**

- Create: `.github/ISSUE_TEMPLATE/add-resource.md`

**Step 1: Write the template**

```markdown
---
name: Add Resource
about: Share a quote, article, video, or other source
title: "[Resource] "
labels: resource, contribution
---

**Resource type:** (quote / article / video / tool / other)

**URL:**

**Title/Description:**

**Why is it relevant to MCP alternatives?**

**Quote to extract (if applicable):**

>

**Author/Source:**
```

**Step 2: Commit**

```bash
git add .github/ISSUE_TEMPLATE/add-resource.md
git commit -m "Add issue template for resource contributions"
```

---

## Phase 8: Final Cleanup

### Task 8.1: Run full regeneration and verify

**Step 1: Run regeneration**

```bash
./mcp-alternatives.regenerate.py
```

**Step 2: Review generated output**

```bash
cat mcp-alternatives.md
```

**Step 3: Run validation**

```bash
./mcp-alternatives/scripts/validate.py
```

**Step 4: Run stats**

```bash
./mcp-alternatives/scripts/stats.py
```

**Step 5: Commit any final changes**

```bash
git add mcp-alternatives.md
git status
git commit -m "Final regeneration after system setup"
```

---

### Task 8.2: Create summary commit

**Step 1: Review all changes**

```bash
git log --oneline -20
```

**Step 2: Push to remote (if desired)**

```bash
git push
```

---

## Summary

After completing all tasks, you will have:

1. **Data files:** `mcp-alternatives/*.{cli,wanted}.yaml`
2. **Specs:** `mcp-alternatives/spec/*.spec.yaml`
3. **Sections:** `mcp-alternatives/sections/*.section.md` and `*.generated`
4. **Scripts:** `validate.py`, `query.py`, `stats.py` in `mcp-alternatives/scripts/`
5. **Main script:** `mcp-alternatives.regenerate.py` at repo root
6. **Agent guide:** `mcp-alternatives/AGENTS.md`
7. **Issue templates:** `.github/ISSUE_TEMPLATE/*.md`
8. **Generated output:** `mcp-alternatives.md`

Contributors can now:
- Add CLI tools via YAML files or issue templates
- Request alternatives via issue templates
- Query and analyze data with scripts
- Regenerate documentation automatically
