# glyph_460.py — Deadline Drum
# -----------------------------------------------------------------------------
# ID:            460
# Pack:          Pack 005 (401–500)
# Name:          Deadline Drum
# Class:         scheduler
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping

def glyph_460(tasks: Sequence[Mapping[str, float]]) -> int:
    """
    Deadline Drum — pick the index of the task with earliest deadline (EDF).

    Overview
    --------
    Break ties by highest priority, then lowest index.

    Parameters
    ----------
    tasks : Sequence[{'deadline':float,'priority':float}]

    Returns
    -------
    int : index or -1 if empty.

    Examples
    --------
    >>> glyph_460([{'deadline':5,'priority':1},{'deadline':3,'priority':2}])
    1

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    if not tasks:
        return -1
    best = None
    idx = -1
    for i, t in enumerate(tasks):
        cand = (float(t.get("deadline", float("inf"))), -float(t.get("priority", 0.0)), i)
        if best is None or cand < best:
            best = cand; idx = i
    return idx
