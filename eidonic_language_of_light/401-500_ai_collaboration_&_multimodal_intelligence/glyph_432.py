# glyph_432.py — Rhythm Tracker
# -----------------------------------------------------------------------------
# ID:            432
# Pack:          Pack 005 (401–500)
# Name:          Rhythm Tracker
# Class:         tracker
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_432(peaks: Sequence[int]) -> List[int]:
    """
    Rhythm Tracker — inter-peak intervals (IPI).

    Overview
    --------
    Returns successive differences of peak indices.

    Parameters
    ----------
    peaks : Sequence[int]

    Returns
    -------
    List[int]

    Examples
    --------
    >>> glyph_432([2, 7, 10])
    [5, 3]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    return [int(peaks[i]-peaks[i-1]) for i in range(1, len(peaks))]
