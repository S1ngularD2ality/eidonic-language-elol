# glyph_284.py — Anchor Flow Limiter
# -----------------------------------------------------------------------------
# ID:            284
# Pack:          Pack 003 (201–300)
# Name:          Anchor Flow Limiter
# Class:         filter
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_284(seq: Sequence[float], *, clip: float) -> List[float]:
    """
    Anchor Flow Limiter — symmetric hard clipper.

    Overview
    --------
    y = sign(x) * min(|x|, clip).

    Parameters
    ----------
    seq : Sequence[float]
    clip : float

    Returns
    -------
    List[float]
        Clipped sequence.

    Examples
    --------
    >>> glyph_284([-10, -1, 0, 0.5, 5], clip=1.0)
    [-1.0, -1.0, 0.0, 0.5, 1.0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    c = abs(float(clip))
    return [max(-c, min(c, float(v))) for v in seq]
