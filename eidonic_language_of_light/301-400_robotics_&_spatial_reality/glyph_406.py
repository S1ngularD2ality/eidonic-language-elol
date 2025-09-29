# glyph_406.py — Task Scheduler
# -----------------------------------------------------------------------------
# ID:            406
# Pack:          Pack 005 (401–500)
# Name:          Task Scheduler
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

def glyph_406(queue: Sequence[Mapping[str, float]]) -> List[int]:
    """
    Task Scheduler — order tasks by (priority desc, deadline asc).

    Overview
    --------
    Returns indices sorted primarily by higher 'priority', secondarily by earlier 'deadline'.

    Parameters
    ----------
    queue : Sequence[{'priority':float,'deadline':float}]

    Returns
    -------
    List[int] : indices of tasks in scheduled order.

    Examples
    --------
    >>> glyph_406([{'priority':1,'deadline':5},{'priority':2,'deadline':9}])
    [1, 0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    indexed = list(enumerate(queue))
    indexed.sort(key=lambda kv: (-float(kv[1].get("priority", 0.0)),
                                 float(kv[1].get("deadline", float("inf")))))
    return [i for i, _ in indexed]
