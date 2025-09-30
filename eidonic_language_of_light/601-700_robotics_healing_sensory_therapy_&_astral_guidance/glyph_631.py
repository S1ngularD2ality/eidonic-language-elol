# glyph_631.py — CLEAN_SURFACE_SCAN
# -----------------------------------------------------------------------------
# ID:            631
# Pack:          Pack 007 (601–700)
# Name:          CLEAN_SURFACE_SCAN
# Class:         analysis_quality
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Dict

def glyph_631(intensity: Sequence[float], *, dirt_threshold: float = 0.15) -> Dict[str, float | bool]:
    """
    CLEAN_SURFACE_SCAN — score cleanliness from normalized intensity samples.

    Overview
    --------
    Treats higher normalized intensity as cleaner; returns cleanliness score and flag.

    Parameters
    ----------
    intensity : Sequence[float]
        Normalized [0,1] values.
    dirt_threshold : float, optional (default: ``0.15``)
        Acceptable dirt fraction (1 - score_clean).

    Returns
    -------
    Dict[str, float | bool]
        {'score_clean': float, 'dirty': bool}

    Examples
    --------
    >>> glyph_631([1,1,0.9,0.8,1])['dirty']
    False

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    n = len(intensity)
    if n == 0:
        return {"score_clean": 1.0, "dirty": False}
    avg = sum(max(0.0, min(1.0, x)) for x in intensity) / n
    score = avg
    return {"score_clean": score, "dirty": score < (1.0 - dirt_threshold)}
