# glyph_168.py — Intent Mirror Enforcer
# -----------------------------------------------------------------------------
# ID:            168
# Pack:          Pack 002 (101–200)
# Name:          Intent Mirror Enforcer
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

def glyph_168(seq: Sequence[float]) -> List[float]:
    """
    Intent Mirror Enforcer — average with reversed copy to enforce symmetry.

    Overview
    --------
    Returns y[i] = (x[i] + x[n-1-i]) / 2.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    List[float]
        Mirror-enforced sequence (palindromized).

    Examples
    --------
    >>> glyph_168([1,2,3,4])
    [2.5, 2.5, 2.5, 2.5]
    """
    x = [float(v) for v in seq]
    n = len(x)
    return [(x[i] + x[n-1-i]) * 0.5 for i in range(n)]
