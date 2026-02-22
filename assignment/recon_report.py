#!/usr/bin/env python3
"""Recon Automation (student skeleton)

You must implement the TODO sections. Keep scope enforcement strict.
Output must match OUTPUT_TEMPLATE_recon.json and OUTPUT_TEMPLATE_recon.md exactly.
"""

import argparse
import json
import socket
import sys
from pathlib import Path
from typing import Any, Dict

# Optional dependency
try:
    import requests  # type: ignore
except Exception:
    requests = None


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def enforce_scope(target: str, scope: Dict[str, Any]) -> None:
    allowed = set(scope.get("allowed_domains", []))
    if target not in allowed:
        raise SystemExit(f"ERROR: Target '{target}' is out of scope. Allowed: {sorted(allowed)}")


def dns_lookup(target: str) -> Dict[str, Any]:
    """Return DNS records (or PTR if target is an IP)."""
    # TODO: implement DNS collection:
    # - If target is an IP: do reverse PTR lookup.
    # - If target is a hostname: collect A/AAAA/MX/NS/TXT (best-effort).
    # - Always record errors instead of crashing.
    return {
        "A": [],
        "AAAA": [],
        "MX": [],
        "NS": [],
        "TXT": [],
        "PTR": [],
        "errors": []
    }


def http_headers(url: str, timeout_s: int = 3) -> Dict[str, Any]:
    """Fetch headers for URL (best-effort)."""
    if requests is None:
        return {"url": url, "status": 0, "headers": {}, "error": "requests not installed"}
    try:
        r = requests.get(url, timeout=timeout_s, allow_redirects=True)
        return {"url": url, "status": int(r.status_code), "headers": dict(r.headers), "error": ""}
    except Exception as e:
        return {"url": url, "status": 0, "headers": {}, "error": str(e)}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--domain", required=True, help="Hostname or IP (use approved IP from TARGETS.md)")
    ap.add_argument("--scope", default="scope.json", help="Path to scope.json")
    ap.add_argument("--out_json", default="recon.json")
    ap.add_argument("--out_md", default="recon.md")
    args = ap.parse_args()

    target = args.domain.strip()
    scope = load_json(Path(args.scope))
    enforce_scope(target, scope)

    # Collect evidence
    dns = dns_lookup(target)
    http = [
        http_headers(f"http://{target}"),
        http_headers(f"https://{target}")
    ]

    out = load_json(Path("OUTPUT_TEMPLATE_recon.json"))
    out["target"]["domain"] = target
    out["dns"] = dns
    out["http"] = http

    Path(args.out_json).write_text(json.dumps(out, indent=2), encoding="utf-8")

    # TODO: generate markdown report matching OUTPUT_TEMPLATE_recon.md
    Path(args.out_md).write_text("TODO: fill recon.md per template\n", encoding="utf-8")

    print(f"Wrote {args.out_json} and {args.out_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
