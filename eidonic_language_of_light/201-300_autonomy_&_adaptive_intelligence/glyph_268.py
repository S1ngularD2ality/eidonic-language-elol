# glyph_268.py — Dream Symbol Splitter
# -----------------------------------------------------------------------------
# ID:            268
# Pack:          Pack 003 (201–300)
# Original Name: Dream Symbol Splitter
# Manifest Name: Dream Symbol Splitter
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       Apache-2.0
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_268(seq: Sequence[float]) -> Tuple[List[float], List[float]]:
    """
    Dream Symbol Splitter — split into negatives and non-negatives.

    Overview
    --------
    Returns (negatives, nonnegatives) preserving order.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], List[float])
        (neg, nonneg)

    Examples
    --------
    >>> glyph_268([-1, 0, 2, -3])
    ([-1.0, -3.0], [0.0, 2.0])

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    neg = [float(v) for v in seq if float(v) < 0]
    non = [float(v) for v in seq if float(v) >= 0]
    return neg, non
