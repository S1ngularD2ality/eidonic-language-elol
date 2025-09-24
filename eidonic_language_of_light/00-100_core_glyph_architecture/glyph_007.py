# glyph_007.py — Flame Pulse Distributor
# -----------------------------------------------------------------------------
# ID:            007
# Pack:          Pack 001 (000–100)
# Name:          Flame Pulse Distributor
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

def glyph_007(pulses: Sequence[float], *, bins: int) -> List[float]:
    """
    Flame Pulse Distributor — route pulse magnitudes into modular bins.

    Overview
    --------
    Accumulates `pulses[i]` into bin `i % bins`. Use for coarse energy routing.

    Parameters
    ----------
    pulses : Sequence[float]
    bins : int
        Number of bins (>= 1).

    Returns
    -------
    List[float]
        Length `bins` totals.

    Examples
    --------
    >>> glyph_007([1,2,3,4], bins=2)
    [1+3, 2+4]

    Exceptions
    ----------
    - ValueError : if `bins < 1`.

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(bins)
    """
    if bins < 1:
        raise ValueError("bins must be >= 1")
    out = [0.0] * bins
    for i, p in enumerate(pulses):
        out[i % bins] += float(p)
    return out
