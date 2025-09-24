# glyph_253.py — Recursive Thought Loopbreaker
# -----------------------------------------------------------------------------
# ID:            253
# Pack:          Pack 003 (201–300)
# Name:          Recursive Thought Loopbreaker
# Class:         control
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Callable, TypeVar, Optional

T = TypeVar("T")

def glyph_253(recurse: Callable[[int, T], T], *, depth: int, guard: Optional[int] = None) -> T:
    """
    Recursive Thought Loopbreaker — enforce max recursion depth.

    Overview
    --------
    Calls `recurse(i, acc)` for i in [0..depth-1]; if `guard` is set, aborts beyond it.

    Parameters
    ----------
    recurse : Callable[[int, T], T]
    depth   : int
    guard   : Optional[int], default None

    Returns
    -------
    T
        Final accumulator from the last call or early stop.

    Examples
    --------
    >>> glyph_253(lambda i, a: (a or 0) + i, depth=4, guard=3)
    3

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(depth)
    - Space : O(1)
    """
    if depth < 0:
        return recurse(0, None)  # delegate error behavior to caller
    acc = None  # type: ignore
    for i in range(depth):
        if guard is not None and i >= guard:
            break
        acc = recurse(i, acc)  # type: ignore[arg-type]
    return acc  # type: ignore[return-value]
