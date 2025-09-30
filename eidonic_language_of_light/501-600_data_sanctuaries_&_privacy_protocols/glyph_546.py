# glyph_546.py — Safe Delete
# -----------------------------------------------------------------------------
# ID:            546
# Pack:          Pack 006 (501–600)
# Name:          Safe Delete
# Class:         planner
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List, Dict

def glyph_546(paths: List[str], *, passes: int = 3, dry_run: bool = True) -> Dict[str, object]:
    """
    Safe Delete — produce an overwrite-then-delete plan (no FS side effects).

    Overview
    --------
    Returns a deterministic **plan** for secure deletion (overwrite patterns + remove).
    This glyph **does not** touch the filesystem; it is a pure planner for runners
    that honor Guardian/Mirror capability gates.

    Parameters
    ----------
    paths : List[str]
        Absolute or project-relative paths to schedule.
    passes : int, optional (default: ``3``)
        Number of overwrite passes.
    dry_run : bool, optional (default: ``True``)
        Always `True` in this glyph; retained for API symmetry.

    Returns
    -------
    Dict[str, object]
        {"plan":"wipe+delete","passes":int,"targets":[...]}.

    Examples
    --------
    >>> plan = glyph_546(["/tmp/a.log"])
    >>> plan["plan"]
    'wipe+delete'

    Exceptions
    ----------
    - ValueError : if a path is empty or contains NUL.

    Complexity
    ----------
    - Time  : O(P)
    - Space : O(P)
    """
    if any((not p) or ("\x00" in p) for p in paths):
        raise ValueError("invalid path")
    return {
        "plan": "wipe+delete",
        "passes": int(max(1, passes)),
        "dry_run": True,
        "targets": sorted(paths),
        "patterns": ["0x00", "0xFF", "random"],
    }
