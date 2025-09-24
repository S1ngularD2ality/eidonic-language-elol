# glyph_249.py — Dream Pulse Extractor
# -----------------------------------------------------------------------------
# ID:            249
# Pack:          Pack 003 (201–300)
# Name:          Dream Pulse Extractor
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_249(seq: Sequence[float], *, threshold: float) -> List[int]:
    """
    Dream Pulse Extractor — indices where |x| exceeds threshold.

    Overview
    --------
    Detects pulse events by absolute amplitude.

    Parameters
    ----------
    seq : Sequence[float]
    threshold : float

    Returns
    -------
    List[int]
        Event indices.

    Examples
    --------
    >>> glyph_249([-0.2, 0.5, 0.1], threshold=0.3)
    [1]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    th = abs(float(threshold))
    return [i for i, v in enumerate(seq) if abs(float(v)) >= th]
