# glyph_272.py — Soul Pulse Diviner
# -----------------------------------------------------------------------------
# ID:            272
# Pack:          Pack 003 (201–300)
# Original Name: Soul Pulse Diviner
# Manifest Name: Soul Pulse Diviner
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_272(seq: Sequence[float], *, threshold: float) -> List[int]:
    """
    Soul Pulse Diviner — indices where |x| crosses threshold.

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
    >>> glyph_272([-0.2, 0.5, 0.1], threshold=0.3)
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
