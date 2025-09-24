# glyph_218.py — Subharmonic Sequence Tracker
# -----------------------------------------------------------------------------
# ID:            218
# Pack:          Pack 003 (201–300)
# Name:          Subharmonic Sequence Tracker
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

def glyph_218(seq: Sequence[float], *, period: int) -> List[float]:
    """
    Subharmonic Sequence Tracker — moving average against a lagged copy.

    Overview
    --------
    Averages x[i] with x[i-period] when i >= period; otherwise passes x[i] through.

    Parameters
    ----------
    seq : Sequence[float]
    period : int
        Positive lag length.

    Returns
    -------
    List[float]
        Tracked sequence.

    Examples
    --------
    >>> glyph_218([1,2,3,4], period=2)
    [1.0, 2.0, 2.0, 3.0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if period < 1:
        return [float(v) for v in seq]
    out: List[float] = []
    for i, v in enumerate(seq):
        if i >= period:
            out.append(0.5 * (float(v) + float(seq[i - period])))
        else:
            out.append(float(v))
    return out
