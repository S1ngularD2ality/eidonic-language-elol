# glyph_251.py — Sequence Pulse Shifter
# -----------------------------------------------------------------------------
# ID:            251
# Pack:          Pack 003 (201–300)
# Name:          Sequence Pulse Shifter
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_251(seq: Sequence[float], *, shift: int) -> List[float]:
    """
    Sequence Pulse Shifter — circularly shift by integer steps.

    Overview
    --------
    y[i] = x[(i - shift) mod n].

    Parameters
    ----------
    seq : Sequence[float]
    shift : int

    Returns
    -------
    List[float]
        Shifted sequence.

    Examples
    --------
    >>> glyph_251([1,2,3,4], shift=1)
    [4.0, 1.0, 2.0, 3.0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    n = len(seq)
    if n == 0:
        return []
    s = ((int(shift) % n) + n) % n
    return [float(seq[(i - s) % n]) for i in range(n)]
