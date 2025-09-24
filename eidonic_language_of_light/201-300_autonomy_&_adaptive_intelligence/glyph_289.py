# glyph_289.py — Harmonic Index Inverter
# -----------------------------------------------------------------------------
# ID:            289
# Pack:          Pack 003 (201–300)
# Name:          Harmonic Index Inverter
# Class:         transform
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_289(seq: Sequence[int], *, n: int | None = None) -> List[int]:
    """
    Harmonic Index Inverter — map index i -> (n-1-i).

    Overview
    --------
    If `n` is None, uses `len(seq)`; values are replaced by inverted positions.

    Parameters
    ----------
    seq : Sequence[int]
    n   : int | None, optional

    Returns
    -------
    List[int]
        Inverted indices.

    Examples
    --------
    >>> glyph_289([0,1,2], n=3)
    [2, 1, 0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    N = int(n) if n is not None else len(seq)
    return [N - 1 - int(v) for v in seq]
