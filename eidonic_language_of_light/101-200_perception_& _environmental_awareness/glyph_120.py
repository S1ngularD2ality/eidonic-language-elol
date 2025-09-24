# glyph_120.py — Dimensional Path Flattener
# -----------------------------------------------------------------------------
# ID:            120
# Pack:          Pack 002 (101–200)
# Name:          Dimensional Path Flattener
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List, Any

def glyph_120(path: Sequence[Tuple[Any, ...]]) -> List[Any]:
    """
    Dimensional Path Flattener — flatten a path of tuples into a single stream.

    Overview
    --------
    [(a,b), (c,d), ...] → [a,b,c,d,...]. Supports tuples of any arity.

    Parameters
    ----------
    path : Sequence[Tuple[Any, ...]]

    Returns
    -------
    List[Any]
        Flattened stream.

    Examples
    --------
    >>> glyph_120([(1,2),(3,4,5)])
    [1, 2, 3, 4, 5]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(total items)
    - Space : O(total items)
    """
    out: List[Any] = []
    for step in path:
        out.extend(step)
    return out
