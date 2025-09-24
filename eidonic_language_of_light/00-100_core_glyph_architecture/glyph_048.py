# glyph_048.py — Polarity Encoder Cascade
# -----------------------------------------------------------------------------
# ID:            048
# Pack:          Pack 001 (000–100)
# Name:          Polarity Encoder Cascade
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_048(seq: Sequence[float]) -> Tuple[List[int], List[int]]:
    """
    Polarity Encoder Cascade — output sign stream and sign-change markers.

    Overview
    --------
    Encodes `signs[i] ∈ {-1,0,1}` and `changes[i] ∈ {0,1}` marking sign flips vs. previous.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.

    Returns
    -------
    (List[int], List[int])
        `(signs, changes)` pair.

    Examples
    --------
    >>> glyph_048([-1, -2, 0, +3, -4])
    ([-1, -1, 0, 1, -1], [0, 0, 1, 1, 1])

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    n = len(seq)
    signs = [0] * n
    for i, v in enumerate(seq):
        x = float(v)
        signs[i] = 0 if x == 0 else (1 if x > 0 else -1)
    changes = [0] * n
    for i in range(1, n):
        changes[i] = 1 if signs[i] != signs[i - 1] else 0
    return signs, changes
