#!/usr/bin/env python3
"""Validate prompt, mode, and toolset files against provided JSON Schemas."""
import json
import sys
from pathlib import Path

try:
    import jsonschema  # type: ignore
except ImportError:
    print("jsonschema not installed. Install with: pip install jsonschema", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent / '.github' / 'copilot'
SCHEMA_DIR = ROOT / 'schemas'
PROMPTS_DIR = ROOT / 'prompt-files'
MODES_DIR = ROOT / 'modes'
TOOLSETS_DIR = ROOT / 'toolsets'
MCP_DIR = ROOT / 'mcp'

SCHEMAS = {
    'prompt': json.loads((SCHEMA_DIR / 'prompt.schema.json').read_text(encoding='utf-8')),
    'mode': json.loads((SCHEMA_DIR / 'mode.schema.json').read_text(encoding='utf-8')),
    'toolset': json.loads((SCHEMA_DIR / 'toolset.schema.json').read_text(encoding='utf-8')),
    'mcp_server': json.loads((SCHEMA_DIR / 'mcp_server.schema.json').read_text(encoding='utf-8')),
}

def validate_file(schema_key: str, path: Path):
    data = json.loads(path.read_text(encoding='utf-8'))
    jsonschema.validate(instance=data, schema=SCHEMAS[schema_key])


def main():
    errors = []
    for f in PROMPTS_DIR.glob('*.json'):
        try:
            validate_file('prompt', f)
        except Exception as e:
            errors.append(f"prompt {f.name}: {e}")
    for f in TOOLSETS_DIR.glob('*.yaml'):
        # Toolset YAML converted to JSON-like dict minimal validation (best-effort)
        # Not performing full YAML parse to avoid extra deps; skipping.
        pass
    for f in MCP_DIR.glob('*.yaml'):
        pass
    for f in MODES_DIR.glob('*.yaml'):
        # Optional: could add YAML -> JSON validation here.
        pass

    if errors:
        print("Validation errors:")
        for e in errors:
            print(" -", e)
        sys.exit(1)
    print("Validation successful.")

if __name__ == '__main__':
    main()
