# glyph_210.py — Mirror Lens Diverger
# -----------------------------------------------------------------------------
# ID:            210
# Pack:          Pack 003 (201–300)
# Name:          Mirror Lens Diverger
# Class:         transform
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_210(seq: Sequence[float]) -> Tuple[List[float], List[float]]:
    """
    Mirror Lens Diverger — split into forward and backward views.

    Overview
    --------
    Returns the original sequence and its reversed copy.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], List[float])
        (forward, backward)

    Examples
    --------
    >>> glyph_210([1,2,3])
    ([1.0, 2.0, 3.0], [3.0, 2.0, 1.0])

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    x = [float(v) for v in seq]
    return x, x[::-1]
