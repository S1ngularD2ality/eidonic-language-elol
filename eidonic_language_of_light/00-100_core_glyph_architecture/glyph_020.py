# glyph_020.py — Soul Harmonic Filter
# -----------------------------------------------------------------------------
# ID:            020
# Pack:          Pack 001 (000–100)
# Name:          Soul Harmonic Filter
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_020(seq: Sequence[float], *, limit: float) -> List[float]:
    """
    Soul Harmonic Filter — clamp magnitudes to an allowed stability threshold.

    Overview
    --------
    Returns values whose absolute magnitude ≤ `limit`.

    Parameters
    ----------
    seq : Sequence[float]
    limit : float

    Returns
    -------
    List[float]
        Filtered sequence.

    Examples
    --------
    >>> glyph_020([-5,-1,0,2,9], limit=2)
    [-1.0, 0.0, 2.0]
    """
    L = abs(float(limit))
    return [float(x) for x in seq if abs(float(x)) <= L]
