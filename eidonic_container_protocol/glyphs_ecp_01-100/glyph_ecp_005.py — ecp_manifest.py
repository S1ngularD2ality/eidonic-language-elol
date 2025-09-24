# glyph_ecp_005.py — ecp_manifest
# -----------------------------------------------------------------------------
# ID:            ecp_005
# Pack:          Pack ECP (Eidonic Container Protocol)
# Name:          ecp_manifest
# Class:         metadata
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-24
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_ecp.md', manifest_json='glyph_manifest_pack_ecp.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from __future__ import annotations
import json, os, hashlib, pathlib, time
from typing import Dict, Any, List

def glyph_ecp_005_ecp_manifest(
    *,
    glyph_dir: str = "glyphs",
    out_path: str = "ecp/manifest.json",
    algo: str = "sha3_256",
    dry_run: bool = False
) -> Dict[str, Any]:
    """
    ecp_manifest — generate/update ECP manifest with provenance & checksums.

    Overview
    --------
    Walks `glyph_dir`, computes file digests (default **SHA3-256**), and writes a versioned
    manifest. Prior manifest (if any) is preserved as a timestamped backup alongside.

    Parameters
    ----------
    glyph_dir : str, optional (default: "glyphs")
        Directory of glyph modules to include.
    out_path : str, optional (default: "ecp/manifest.json")
        Destination manifest path.
    algo : str, optional (default: "sha3_256")
        Hash algorithm available via `hashlib`.
    dry_run : bool, optional (default: False)
        If True, compute values but do not write files.

    Returns
    -------
    Dict[str, Any]
        {"path": <out_path>, "count": int, "hashes": [{path, algo, digest}], "backup": <or None>}

    Examples
    --------
    >>> out = glyph_ecp_005_ecp_manifest(glyph_dir="glyphs_ecp_01-100", dry_run=True)
    >>> isinstance(out["hashes"], list)
    True

    Exceptions
    ----------
    - FileNotFoundError : if `glyph_dir` missing.
    - ValueError        : if `algo` unsupported by `hashlib`.

    Complexity
    ----------
    - Time  : O(n · file_size)
    - Space : O(n)
    """
    if not hasattr(hashlib, algo):
        raise ValueError(f"Unsupported hash algorithm: {algo}")

    gdir = pathlib.Path(glyph_dir).resolve()
    if not gdir.exists():
        raise FileNotFoundError(f"Glyph directory not found: {gdir}")

    files: List[pathlib.Path] = sorted(p for p in gdir.rglob("*.py") if p.is_file())
    hlist: List[Dict[str, str]] = []

    for p in files:
        h = getattr(hashlib, algo)()
        with p.open("rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        hlist.append({"path": str(p), "algo": algo, "digest": h.hexdigest()})

    manifest = {
        "created_ns": time.time_ns(),
        "algo": algo,
        "root": str(gdir),
        "count": len(files),
        "hashes": hlist,
    }

    backup = None
    if not dry_run:
        out = pathlib.Path(out_path).resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        if out.exists():
            backup = out.with_suffix(out.suffix + f".bak.{int(time.time())}")
            out.replace(backup)
        with out.open("w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)

    return {"path": out_path, "count": len(files), "hashes": hlist, "backup": str(backup) if backup else None}
