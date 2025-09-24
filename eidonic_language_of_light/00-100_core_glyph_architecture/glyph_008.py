# glyph_008.py — Dream Cycle Encoder
# -----------------------------------------------------------------------------
# ID:            008
# Pack:          Pack 001 (000–100)
# Name:          Dream Cycle Encoder
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_008(seq: Sequence[int], *, loops: int) -> List[int]:
    """
    Dream Cycle Encoder — tile a base pattern `loops` times.

    Overview
    --------
    Encodes repetition as a simple cycle expansion.

    Parameters
    ----------
    seq : Sequence[int]
        Base motif.
    loops : int
        Number of repetitions (>= 1).

    Returns
    -------
    List[int]
        Tiled sequence.

    Examples
    --------
    >>> glyph_008([1,2], loops=3)
    [1,2,1,2,1,2]

    Exceptions
    ----------
    - ValueError : if `loops < 1`.

    Complexity
    ----------
    - Time  : O(n·loops)
    - Space : O(n·loops)
    """
    if loops < 1:
        raise ValueError("loops must be >= 1")
    return [int(v) for _ in range(loops) for v in seq]
