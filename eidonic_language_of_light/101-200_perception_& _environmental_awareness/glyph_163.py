# glyph_163.py — Phase Core Expander
# -----------------------------------------------------------------------------
# ID:            163
# Pack:          Pack 002 (101–200)
# Name:          Phase Core Expander
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_163(seq: Sequence[float], *, factor: int = 2) -> List[float]:
    """
    Phase Core Expander — insert linear midpoints between samples.

    Overview
    --------
    For each adjacent pair, inserts (factor-1) evenly spaced interpolants, expanding
    length to (n-1)*factor + 1.

    Parameters
    ----------
    seq : Sequence[float]
    factor : int, optional (default: 2)  # >= 1

    Returns
    -------
    List[float]
        Expanded sequence.

    Examples
    --------
    >>> glyph_163([0, 2], factor=3)
    [0.0, 1.0, 2.0]

    Exceptions
    ----------
    - ValueError : if factor < 1.

    Complexity
    ----------
    - Time  : O(n·factor)
    - Space : O(n·factor)
    """
    if factor < 1:
        raise ValueError("factor must be >= 1")
    n = len(seq)
    if n == 0:
        return []
    if n == 1 or factor == 1:
        return [float(v) for v in seq]
    out: List[float] = []
    for i in range(n-1):
        a = float(seq[i]); b = float(seq[i+1])
        for t in range(factor):
            out.append(a + (b-a)*(t/float(factor)))
    out.append(float(seq[-1]))
    return out
