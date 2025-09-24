# glyph_213.py — Timeline Disruption Mapper
# -----------------------------------------------------------------------------
# ID:            213
# Pack:          Pack 003 (201–300)
# Name:          Timeline Disruption Mapper
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_213(seq: Sequence[float], *, tol: float = 1e-6) -> List[int]:
    """
    Timeline Disruption Mapper — return indices of discontinuities.

    Overview
    --------
    Flags positions where |x[i] - x[i-1]| > tol (i >= 1).

    Parameters
    ----------
    seq : Sequence[float]
    tol : float, optional (default: 1e-6)

    Returns
    -------
    List[int]
        Indices of disruptions.

    Examples
    --------
    >>> glyph_213([0,0,1,1,3], tol=0.5)
    [2, 4]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    out: List[int] = []
    prev = None
    for i, v in enumerate(seq):
        fv = float(v)
        if i and prev is not None and abs(fv - prev) > tol:
            out.append(i)
        prev = fv
    return out
