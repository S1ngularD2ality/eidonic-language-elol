# glyph_433.py — Beat to Intent
# -----------------------------------------------------------------------------
# ID:            433
# Pack:          Pack 005 (401–500)
# Name:          Beat to Intent
# Class:         interpreter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_433(bpm: float, accents: Sequence[int]) -> str:
    """
    Beat to Intent — map tempo & accents to a coarse intent tag.

    Overview
    --------
    bpm < 70 → "calm"; 70–119 → "neutral"; ≥120 → "urgent". Adds "-syncopated" if
    gaps > 1 exist between adjacent accent indices.

    Parameters
    ----------
    bpm : float
    accents : Sequence[int]

    Returns
    -------
    str

    Examples
    --------
    >>> glyph_433(130, [0,2,5,6])
    'urgent-syncopated'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    tag = "calm" if bpm < 70 else ("neutral" if bpm < 120 else "urgent")
    syncopated = any(j-i > 1 for i,j in zip(accents, accents[1:]))
    return tag + ("-syncopated" if syncopated else "")
