# glyph_225.py — Light Thread Collapser
# -----------------------------------------------------------------------------
# ID:            225
# Pack:          Pack 003 (201–300)
# Name:          Light Thread Collapser
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_225(seq: Sequence[float]) -> float:
    """
    Light Thread Collapser — collapse to mirror-consistent scalar.

    Overview
    --------
    Returns the mean of x averaged with reversed(x), i.e., the center of mirror mass.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    float
        Mirror-collapsed scalar.

    Examples
    --------
    >>> glyph_225([1,2,3,4])
    2.5
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0:
        return 0.0
    m = [(x[i] + x[n-1-i]) * 0.5 for i in range(n)]
    return sum(m) / n
