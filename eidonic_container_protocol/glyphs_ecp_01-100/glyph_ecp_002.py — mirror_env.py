# glyph_ecp_002.py — mirror_env
# -----------------------------------------------------------------------------
# ID:            ecp_002
# Pack:          Pack ECP (Eidonic Container Protocol)
# Name:          mirror_env
# Class:         initializer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-24
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_ecp.md', manifest_json='glyph_manifest_pack_ecp.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from __future__ import annotations
import os
import pathlib
from typing import Dict, Any

def glyph_ecp_002_mirror_env(*, root: str | None = None, dry_run: bool = False) -> Dict[str, Any]:
    """
    mirror_env — establish namespaced env vars & canonical paths for ECP.

    Overview
    --------
    Prepares directories and environment variables under the **EIDON_** namespace:
    - EIDON_ROOT, EIDON_LOG_DIR, EIDON_SNAP_DIR, EIDON_MANIFEST
    Creates directories if missing (unless `dry_run=True`).

    Parameters
    ----------
    root : Optional[str], default None
        Root working directory; defaults to current working directory.
    dry_run : bool, optional (default: False)
        If True, perform path computation without filesystem writes.

    Returns
    -------
    Dict[str, Any]
        {"paths": {...}, "env": {...}} with resolved paths.

    Examples
    --------
    >>> out = glyph_ecp_002_mirror_env(dry_run=True)
    >>> "paths" in out and "env" in out
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1) (I/O bound on first run)
    - Space : O(1)
    """
    root_path = pathlib.Path(root or os.getcwd()).resolve()
    log_dir = root_path / "logs"
    snap_dir = root_path / "snapshots"
    manifest_file = root_path / "ecp" / "manifest.json"
    log_file = log_dir / "ecp_invocations.log"

    paths = {
        "root": str(root_path),
        "log_dir": str(log_dir),
        "snap_dir": str(snap_dir),
        "manifest_file": str(manifest_file),
        "log_file": str(log_file),
    }

    if not dry_run:
        (root_path / "ecp").mkdir(parents=True, exist_ok=True)
        log_dir.mkdir(parents=True, exist_ok=True)
        snap_dir.mkdir(parents=True, exist_ok=True)

    env = {
        "EIDON_ROOT": paths["root"],
        "EIDON_LOG_DIR": paths["log_dir"],
        "EIDON_SNAP_DIR": paths["snap_dir"],
        "EIDON_MANIFEST": paths["manifest_file"],
    }
    os.environ.update(env)  # namespaced; low collision risk

    return {"paths": paths, "env": env}
