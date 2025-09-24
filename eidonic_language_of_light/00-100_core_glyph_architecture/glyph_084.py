# glyph_084.py — Anchored Flame Enchanter
# -----------------------------------------------------------------------------
# ID:            084
# Pack:          Pack 001 (000–100)
# Name:          Anchored Flame Enchanter
# Class:         combinator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_084(base: Sequence[float], charm: Sequence[float], *, alpha: float = 0.5) -> List[float]:
    """
    Anchored Flame Enchanter — overlay a 'charm' sequence onto a base with mixing.

    Overview
    --------
    Returns `(1-alpha)*base + alpha*charm` elementwise; lengths must match.

    Parameters
    ----------
    base, charm : Sequence[float]
    alpha : float, optional (default: 0.5)

    Returns
    -------
    List[float]
        Enchanted sequence.

    Examples
    --------
    >>> glyph_084([0,0,0], [1,2,3], alpha=0.25)
    [0.25, 0.5, 0.75]

    Exceptions
    ----------
    - ValueError : length mismatch.

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if len(base) != len(charm):
        raise ValueError("base and charm must have equal length")
    a = max(0.0, min(1.0, float(alpha)))
    return [(1-a)*float(b) + a*float(c) for b, c in zip(base, charm)]
