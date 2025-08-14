#!/usr/bin/env python3
"""Generate expanded instruction markdown per mode.
Expands tag references (#context, @extension, /command) in prompt files.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / '.github' / 'copilot'
CONTEXT_DIR = ROOT / 'context'
EXT_DIR = ROOT / 'extensions'
CMD_DIR = ROOT / 'commands'
MODES_DIR = ROOT / 'modes'
PROMPTS_DIR = ROOT / 'prompt-files'
RUNTIME_DIR = ROOT / 'runtime'

TAG_CONTEXT = re.compile(r'#([a-zA-Z0-9_\-]+)')
TAG_EXTENSION = re.compile(r'@([a-zA-Z0-9_\-]+)')
TAG_COMMAND = re.compile(r'/([a-zA-Z0-9_\-]+)')


def load_text_map(directory: Path) -> dict:
    data = {}
    for file in directory.glob('*.*'):
        data[file.stem] = file.read_text(encoding='utf-8').strip()
    return data


def expand_tags(instruction: str, ctx_map: dict, ext_map: dict, cmd_map: dict) -> str:
    def repl_context(m):
        key = m.group(1)
        return f"\n<!-- #{key} -->\n" + ctx_map.get(key, f"[MISSING CONTEXT:{key}]") + "\n"
    def repl_extension(m):
        key = m.group(1)
        return f"\n<!-- @{key} -->\n" + ext_map.get(key, f"[MISSING EXTENSION:{key}]") + "\n"
    def repl_command(m):
        key = m.group(1)
        return f"\n<!-- /{key} -->\n" + cmd_map.get(key, f"[MISSING COMMAND:{key}]") + "\n"

    expanded = TAG_CONTEXT.sub(repl_context, instruction)
    expanded = TAG_EXTENSION.sub(repl_extension, expanded)
    expanded = TAG_COMMAND.sub(repl_command, expanded)
    return expanded.strip() + '\n'


def main():
    ctx_map = load_text_map(CONTEXT_DIR)
    ext_map = load_text_map(EXT_DIR)
    cmd_map = load_text_map(CMD_DIR)

    RUNTIME_DIR.mkdir(exist_ok=True)

    # Group prompt files by mode
    grouped = {}
    for p in PROMPTS_DIR.glob('*.json'):
        data = json.loads(p.read_text(encoding='utf-8'))
        mode = data.get('tags', {}).get('mode') or 'default'
        grouped.setdefault(mode, []).append(data)

    for mode, prompts in grouped.items():
        parts = [f"# Mode: {mode}\n"]
        for prompt in prompts:
            parts.append(f"## {prompt['name']} ({prompt['id']})\n")
            parts.append(expand_tags(prompt['instructions'], ctx_map, ext_map, cmd_map))
        out_file = RUNTIME_DIR / f"instructions.{mode}.md"
        out_file.write_text('\n'.join(parts), encoding='utf-8')
        print(f"Generated {out_file}")

if __name__ == '__main__':
    main()
