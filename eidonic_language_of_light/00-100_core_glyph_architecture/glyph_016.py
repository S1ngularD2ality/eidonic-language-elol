# glyph_016.py — Liminal Flame Extractor
# -----------------------------------------------------------------------------
# ID:            016
# Pack:          Pack 001 (000–100)
# Name:          Liminal Flame Extractor
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_016(seq: Sequence[float], *, threshold: float) -> List[int]:
    """
    Liminal Flame Extractor — detect indices where magnitude crosses a threshold.

    Overview
    --------
    Returns positions i where |x[i]| >= threshold; a simple “liminal” activator.

    Parameters
    ----------
    seq : Sequence[float]
    threshold : float

    Returns
    -------
    List[int]
        Activated indices.

    Examples
    --------
    >>> glyph_016([0, 0.5, 2.0, 0.1], threshold=1.0)
    [2]
    """
    return [i for i, v in enumerate(seq) if abs(float(v)) >= float(threshold)]
