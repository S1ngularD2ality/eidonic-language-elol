# glyph_299.py — Mirror Intent Loopbreaker
# -----------------------------------------------------------------------------
# ID:            299
# Pack:          Pack 003 (201–300)
# Name:          Mirror Intent Loopbreaker
# Class:         control
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Callable, Optional, TypeVar

R = TypeVar("R")

def glyph_299(step: Callable[[int, Optional[R]], R], *, max_steps: int, break_on: Callable[[R], bool]) -> R:
    """
    Mirror Intent Loopbreaker — iterate with intent check; stop on mirrored condition.

    Overview
    --------
    Repeatedly calls step(i, acc); after each call, if break_on(acc) is True, stops.

    Parameters
    ----------
    step : Callable[[int, Optional[R]], R]
    max_steps : int
    break_on : Callable[[R], bool]

    Returns
    -------
    R
        Final accumulator (last produced value).

    Examples
    --------
    >>> glyph_299(lambda i,a: (a or 0)+i, max_steps=5, break_on=lambda acc: acc>=6)
    6

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(max_steps)
    - Space : O(1)
    """
    acc: Optional[R] = None
    for i in range(max(0, int(max_steps))):
        acc = step(i, acc)
        if break_on(acc):  # type: ignore[arg-type]
            break
    return acc  # type: ignore[return-value]
