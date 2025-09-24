# glyph_125.py — Spiral Key Reorienter
# -----------------------------------------------------------------------------
# ID:            125
# Pack:          Pack 002 (101–200)
# Name:          Spiral Key Reorienter
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

def glyph_125(key: Sequence[int], *, rotate: int = 0, flip: bool = False) -> List[int]:
    """
    Spiral Key Reorienter — rotate and optionally reverse a traversal key.

    Overview
    --------
    Circularly rotates by `rotate` steps; if `flip`, reverse after rotation.

    Parameters
    ----------
    key : Sequence[int]
    rotate : int, optional (default: 0)
    flip : bool, optional (default: False)

    Returns
    -------
    List[int]
        Reoriented key.

    Examples
    --------
    >>> glyph_125([0,1,2,3], rotate=1, flip=True)
    [2, 1, 0, 3]
    """
    n = len(key)
    if n == 0:
        return []
    r = ((rotate % n) + n) % n
    out = [int(key[(i - r) % n]) for i in range(n)]
    if flip:
        out.reverse()
    return out
