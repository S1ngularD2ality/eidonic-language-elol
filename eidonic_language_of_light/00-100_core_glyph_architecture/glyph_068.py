# glyph_068.py — Phase Shift Activator
# -----------------------------------------------------------------------------
# ID:            068
# Pack:          Pack 001 (000–100)
# Name:          Phase Shift Activator
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_068(seq: Sequence[float], *, shift: int) -> List[float]:
    """
    Phase Shift Activator — circularly rotate a sequence by `shift`.

    Overview
    --------
    Positive shift moves elements forward (to higher indices), wrapping around.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.
    shift : int
        Rotation amount (can be negative).

    Returns
    -------
    List[float]
        Rotated sequence.

    Examples
    --------
    >>> glyph_068([1,2,3,4], shift=2)
    [3.0, 4.0, 1.0, 2.0]

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
    k = shift % n
    return [float(seq[(i - k) % n]) for i in range(n)]
