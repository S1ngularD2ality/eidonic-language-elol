# glyph_ecp_003.py — glyph_loader
# -----------------------------------------------------------------------------
# ID:            ecp_003
# Pack:          Pack ECP (Eidonic Container Protocol)
# Name:          glyph_loader
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-24
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_ecp.md', manifest_json='glyph_manifest_pack_ecp.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from __future__ import annotations
import importlib.util
import pathlib
from typing import Dict, Any, List

def glyph_ecp_003_glyph_loader(*, glyph_dir: str = "glyphs", dry_run: bool = False) -> Dict[str, Any]:
    """
    glyph_loader — discover glyph modules safely from a directory.

    Overview
    --------
    Enumerates Python files named like ``glyph_*.py`` under `glyph_dir`.
    In non-dry runs, attempts **safe module loading** via `importlib.util.spec_from_file_location`
    with directory restriction (no arbitrary paths). Execution of top-level code is the Python
    import model; glyphs should be pure at import time.

    Parameters
    ----------
    glyph_dir : str, optional (default: "glyphs")
        Directory to scan.
    dry_run : bool, optional (default: False)
        If True, only list candidates without loading.

    Returns
    -------
    Dict[str, Any]
        {"dir": <resolved>, "files": [..], "loaded": [module_names]} (loaded empty in `dry_run`).

    Examples
    --------
    >>> out = glyph_ecp_003_glyph_loader(glyph_dir="glyphs_ecp_01-100", dry_run=True)
    >>> isinstance(out["files"], list)
    True

    Exceptions
    ----------
    - FileNotFoundError : if `glyph_dir` does not exist.
    - ImportError       : if a module fails to load (non-dry run).

    Complexity
    ----------
    - Time  : O(n) for n files
    - Space : O(n)
    """
    base = pathlib.Path(glyph_dir).resolve()
    if not base.exists():
        raise FileNotFoundError(f"Glyph directory not found: {base}")
    candidates: List[pathlib.Path] = sorted(p for p in base.glob("glyph_*.py") if p.is_file())

    loaded: List[str] = []
    if not dry_run:
        for path in candidates:
            # Restrict to the chosen directory
            if base not in path.parents and path.parent != base:
                continue
            mod_name = f"eidon_glyphs.{path.stem}"
            spec = importlib.util.spec_from_file_location(mod_name, str(path))
            if spec and spec.loader:
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)  # pylint: disable=exec-used
                loaded.append(mod.__name__)
    return {"dir": str(base), "files": [str(p) for p in candidates], "loaded": loaded}
