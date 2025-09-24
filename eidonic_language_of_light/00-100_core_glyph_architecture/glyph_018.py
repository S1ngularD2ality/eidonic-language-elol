# glyph_018.py — Mirror Phase Comparator
# -----------------------------------------------------------------------------
# ID:            018
# Pack:          Pack 001 (000–100)
# Name:          Mirror Phase Comparator
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_018(seq: Sequence[float]) -> float:
    """
    Mirror Phase Comparator — cosine similarity between a sequence and its reverse.

    Overview
    --------
    Measures mirror alignment ∈ [-1,1].

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    float
        Cosine similarity with reversed sequence.

    Examples
    --------
    >>> round(glyph_018([1,2,3,2,1]), 3)
    1.0
    """
    x = [float(v) for v in seq]
    y = list(reversed(x))
    dot = sum(a*b for a,b in zip(x,y))
    nx = (sum(a*a for a in x) ** 0.5) or 1.0
    ny = (sum(b*b for b in y) ** 0.5) or 1.0
    return dot/(nx*ny)
