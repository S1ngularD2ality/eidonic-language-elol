# glyph_057.py — Polarity Sequence Tracker
# -----------------------------------------------------------------------------
# ID:            057
# Pack:          Pack 001 (000–100)
# Name:          Polarity Sequence Tracker
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

def glyph_057(seq: Sequence[float]) -> List[int]:
    """
    Polarity Sequence Tracker — cumulative count of sign changes.

    Overview
    --------
    Emits `c[i]` equal to the number of sign flips observed up to index `i`.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.

    Returns
    -------
    List[int]
        Cumulative sign-change counts.

    Examples
    --------
    >>> glyph_057([1, -1, -2, 0, 3])
    [0, 1, 1, 2, 3]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    out: List[int] = []
    last = 0
    count = 0
    for v in seq:
        s = 0 if v == 0 else (1 if v > 0 else -1)
        if out:
            if s != last:
                count += 1
        out.append(count)
        last = s
    return out
