# glyph_455.py — Escalation Ladder
# -----------------------------------------------------------------------------
# ID:            455
# Pack:          Pack 005 (401–500)
# Name:          Escalation Ladder
# Class:         policy
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_455(levels: Sequence[str], *, step: int, max_level: int | None = None) -> str:
    """
    Escalation Ladder — select a level by step index with optional cap.

    Overview
    --------
    Clamps step to [0, max_level or last] and returns levels[step].

    Parameters
    ----------
    levels    : Sequence[str]
    step      : int
    max_level : Optional[int]

    Returns
    -------
    str

    Examples
    --------
    >>> glyph_455(["info","warn","page"], step=2)
    'page'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if not levels:
        return ""
    cap = len(levels) - 1 if max_level is None else max(0, min(len(levels) - 1, int(max_level)))
    s = max(0, min(cap, int(step)))
    return levels[s]
