# glyph_ecp_004.py — container_seal
# -----------------------------------------------------------------------------
# ID:            ecp_004
# Pack:          Pack ECP (Eidonic Container Protocol)
# Name:          container_seal
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-24
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_ecp.md', manifest_json='glyph_manifest_pack_ecp.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from __future__ import annotations
import json, time, os, pathlib
from typing import Dict, Any

def glyph_ecp_004_container_seal(*, log_path: str, dry_run: bool = False, rotate_bytes: int = 2_000_000) -> Dict[str, Any]:
    """
    container_seal — write a structured seal entry with lightweight rotation.

    Overview
    --------
    Appends a JSON line to the invocation log: timestamp (ns), pid, cwd, status="sealed".
    If log exceeds `rotate_bytes`, rotates to `*.1` (single-epoch simple rotation).

    Parameters
    ----------
    log_path : str
        Final path to the seal log file.
    dry_run : bool, optional (default: False)
        If True, return the would-be entry without writing.
    rotate_bytes : int, optional (default: 2_000_000)
        File size threshold for rotation.

    Returns
    -------
    Dict[str, Any]
        {"entry": <dict>, "path": <log_path>, "rotated": bool}

    Examples
    --------
    >>> out = glyph_ecp_004_container_seal(log_path="logs/ecp_invocations.log", dry_run=True)
    >>> out["entry"]["status"] == "sealed"
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1) (I/O)
    - Space : O(1)
    """
    entry = {
        "ts_ns": time.time_ns(),
        "pid": os.getpid(),
        "cwd": os.getcwd(),
        "status": "sealed",
    }
    rotated = False

    if dry_run:
        return {"entry": entry, "path": log_path, "rotated": rotated}

    path = pathlib.Path(log_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists() and path.stat().st_size >= max(1, int(rotate_bytes)):
        backup = path.with_suffix(path.suffix + ".1")
        if backup.exists():
            backup.unlink()
        path.replace(backup)
        rotated = True

    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    return {"entry": entry, "path": str(path), "rotated": rotated}
