# glyph_198.py — Flame Gate Splitter
# -----------------------------------------------------------------------------
# ID:            198
# Pack:          Pack 002 (101–200)
# Name:          Flame Gate Splitter
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_198(seq: Sequence[float], *, low: float, high: float) -> Tuple[List[float], List[float], List[float]]:
    """
    Flame Gate Splitter — tri-partition by thresholds.

    Overview
    --------
    Splits into (below_low, within_[low,high], above_high) preserving order.

    Parameters
    ----------
    seq : Sequence[float]
    low : float
    high : float

    Returns
    -------
    (List[float], List[float], List[float])
        (below, within, above)

    Examples
    --------
    >>> glyph_198([0,1,2,3], low=1, high=2)
    ([0.0], [1.0, 2.0], [3.0])
    """
    lo, hi = (low, high) if low <= high else (high, low)
    below = [float(v) for v in seq if float(v) < lo]
    within = [float(v) for v in seq if lo <= float(v) <= hi]
    above = [float(v) for v in seq if float(v) > hi]
    return below, within, above
