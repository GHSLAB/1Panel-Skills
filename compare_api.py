#!/usr/bin/env python3
"""Compare two Swagger/OpenAPI JSON documents and report API differences in Markdown."""

import json
import sys


def load_doc(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def get_paths(doc: dict) -> dict:
    return doc.get("paths", {})


def get_methods(path_obj: dict) -> list:
    return [m for m in path_obj if m in ("get", "post", "put", "delete", "patch", "options", "head")]


def compare_api_details(v1_obj: dict, v2_obj: dict) -> list:
    diffs = []
    for method in get_methods(v1_obj):
        if method not in v2_obj:
            continue
        v1_op = v1_obj[method]
        v2_op = v2_obj[method]
        if v1_op.get("summary") != v2_op.get("summary"):
            diffs.append(f"`summary`: `{v1_op.get('summary')}` → `{v2_op.get('summary')}`")
        if v1_op.get("tags") != v2_op.get("tags"):
            diffs.append(f"`tags`: `{v1_op.get('tags')}` → `{v2_op.get('tags')}`")
        v1_params = v1_op.get("parameters", [])
        v2_params = v2_op.get("parameters", [])
        if len(v1_params) != len(v2_params):
            diffs.append(f"`parameters`: `{len(v1_params)}` → `{len(v2_params)}`")
        else:
            for i, (p1, p2) in enumerate(zip(v1_params, v2_params)):
                if p1.get("name") != p2.get("name"):
                    diffs.append(f"`param[{i}] name`: `{p1.get('name')}` → `{p2.get('name')}`")
                if p1.get("in") != p2.get("in"):
                    diffs.append(f"`param[{i}] in`: `{p1.get('in')}` → `{p2.get('in')}`")
                if p1.get("required") != p2.get("required"):
                    diffs.append(f"`param[{i}] required`: `{p1.get('required')}` → `{p2.get('required')}`")
        v1_responses = list(v1_op.get("responses", {}).keys())
        v2_responses = list(v2_op.get("responses", {}).keys())
        if v1_responses != v2_responses:
            diffs.append(f"`responses`: `{v1_responses}` → `{v2_responses}`")
    return diffs


def main():
    if len(sys.argv) < 3:
        print("Usage: python compare_api.py doc_v1.json doc_v2.json [output.md]")
        sys.exit(1)

    v1 = load_doc(sys.argv[1])
    v2 = load_doc(sys.argv[2])
    output_file = sys.argv[3] if len(sys.argv) > 3 else None

    v1_paths = get_paths(v1)
    v2_paths = get_paths(v2)

    v1_methods = {(p, m) for p in v1_paths for m in get_methods(v1_paths[p])}
    v2_methods = {(p, m) for p in v2_paths for m in get_methods(v2_paths[p])}

    added = v2_methods - v1_methods
    removed = v1_methods - v2_methods
    common = v1_methods & v2_methods

    lines = []
    lines.append("# API Comparison Report\n")
    lines.append(f"| Item | v1 | v2 |")
    lines.append(f"|------|----|----|")
    lines.append(f"| Base Path | `{v1.get('basePath', 'N/A')}` | `{v2.get('basePath', 'N/A')}` |")
    lines.append(f"| Version | `{v1.get('info', {}).get('version', 'N/A')}` | `{v2.get('info', {}).get('version', 'N/A')}` |")
    lines.append("")

    lines.append(f"## Summary: Added={len(added)}, Removed={len(removed)}, Modified=... (see below)\n")

    lines.append(f"## Added APIs ({len(added)})\n")
    if added:
        lines.append("| Method | Path | Summary |")
        lines.append("|--------|------|---------|")
        for path, method in sorted(added):
            obj = v2_paths[path][method]
            summary = obj.get("summary") or "N/A"
            lines.append(f"| `{method.upper()}` | `{path}` | {summary} |")
    else:
        lines.append("_none_\n")
    lines.append("")

    lines.append(f"## Removed APIs ({len(removed)})\n")
    if removed:
        lines.append("| Method | Path | Summary |")
        lines.append("|--------|------|---------|")
        for path, method in sorted(removed):
            obj = v1_paths[path][method]
            summary = obj.get("summary") or "N/A"
            lines.append(f"| `{method.upper()}` | `{path}` | {summary} |")
    else:
        lines.append("_none_\n")
    lines.append("")

    lines.append(f"## Modified APIs ({len(common)})\n")
    modified_count = 0
    if common:
        lines.append("| Method | Path | Changes |")
        lines.append("|--------|------|---------|")
        for path, method in sorted(common):
            diffs = compare_api_details(v1_paths[path], v2_paths[path])
            if diffs:
                modified_count += 1
                changes = " | ".join(diffs)
                lines.append(f"| `{method.upper()}` | `{path}` | {changes} |")

    lines[4] = f"## Summary: Added={len(added)}, Removed={len(removed)}, Modified={modified_count}\n"

    md = "\n".join(lines)

    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(md)
        print(f"Markdown report saved to: {output_file}")
    else:
        print(md)


if __name__ == "__main__":
    main()
