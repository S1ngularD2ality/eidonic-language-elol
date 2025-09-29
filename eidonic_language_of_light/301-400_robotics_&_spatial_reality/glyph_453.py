# glyph_453.py — Shard Planner
# -----------------------------------------------------------------------------
# ID:            453
# Pack:          Pack 005 (401–500)
# Name:          Shard Planner
# Class:         planner
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Dict, List

def glyph_453(tasks: Sequence[str], shards: Sequence[str]) -> Dict[str, List[str]]:
    """
    Shard Planner — round-robin assignment of tasks to shard ids.

    Overview
    --------
    Deterministic modulo assignment by task index.

    Parameters
    ----------
    tasks  : Sequence[str]
    shards : Sequence[str]

    Returns
    -------
    Dict[str,List[str]] : shard_id → [tasks]

    Examples
    --------
    >>> glyph_453(["t1","t2","t3"], ["A","B"])
    {'A': ['t1', 't3'], 'B': ['t2']}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(T)
    - Space : O(T)
    """
    out: Dict[str, List[str]] = {s: [] for s in shards}
    if not shards:
        return out
    k = len(shards)
    for i, t in enumerate(tasks):
        out[shards[i % k]].append(str(t))
    return out
