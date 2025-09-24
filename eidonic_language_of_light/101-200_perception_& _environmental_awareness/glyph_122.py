# glyph_122.py — Soul Sequence Stabilizer
# -----------------------------------------------------------------------------
# ID:            122
# Pack:          Pack 002 (101–200)
# Name:          Soul Sequence Stabilizer
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_122(seq: Sequence[float], *, alpha: float = 0.2) -> List[float]:
    """
    Soul Sequence Stabilizer — exponential moving average (EMA).

    Overview
    --------
    Applies y[t] = α·x[t] + (1-α)·y[t-1] with y[0]=x[0].

    Parameters
    ----------
    seq : Sequence[float]
    alpha : float, optional (default: 0.2)

    Returns
    -------
    List[float]
        Smoothed sequence.

    Examples
    --------
    >>> glyph_122([0,1,0,1], alpha=0.5)
    [0.0, 0.5, 0.25, 0.625]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if not seq:
        return []
    a = max(0.0, min(1.0, float(alpha)))
    y = [float(seq[0])]
    for v in seq[1:]:
        y.append(a*float(v) + (1-a)*y[-1])
    return y
