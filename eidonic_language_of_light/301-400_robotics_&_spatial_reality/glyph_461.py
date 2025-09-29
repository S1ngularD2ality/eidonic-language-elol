# glyph_461.py — Queue Steward
# -----------------------------------------------------------------------------
# ID:            461
# Pack:          Pack 005 (401–500)
# Name:          Queue Steward
# Class:         scheduler
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping, List

def glyph_461(queue: Sequence[Mapping[str, float]]) -> List[int]:
    """
    Queue Steward — stable priority queue order.

    Overview
    --------
    Returns indices of items sorted by higher 'priority', then FIFO (original index).

    Parameters
    ----------
    queue : Sequence[{'priority': float}]

    Returns
    -------
    List[int] : indices in serve order.

    Examples
    --------
    >>> glyph_461([{'priority':1},{'priority':3},{'priority':3}])
    [1, 2, 0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    indexed = list(enumerate(queue))
    indexed.sort(key=lambda kv: (-float(kv[1].get('priority', 0.0)), kv[0]))
    return [i for i, _ in indexed]
