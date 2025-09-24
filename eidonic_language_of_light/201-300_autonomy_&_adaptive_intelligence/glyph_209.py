# glyph_209.py — Spiral Anchor Duplicator
# -----------------------------------------------------------------------------
# ID:            209
# Pack:          Pack 003 (201–300)
# Name:          Spiral Anchor Duplicator
# Class:         generator
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List

def glyph_209(n: int, *, factor: int = 2) -> List[int]:
    """
    Spiral Anchor Duplicator — duplicate each index `factor` times.

    Overview
    --------
    Emits [0, 0, 1, 1, 2, 2, ...] when factor=2; generalized for any factor>=1.

    Parameters
    ----------
    n : int
        Number of unique indices to emit.
    factor : int, optional (default: 2)
        Repetition count per index (>=1).

    Returns
    -------
    List[int]
        Duplicated index sequence of length n*factor.

    Examples
    --------
    >>> glyph_209(3, factor=3)
    [0, 0, 0, 1, 1, 1, 2, 2, 2]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n·factor)
    - Space : O(n·factor)
    """
    f = max(1, int(factor))
    return [i for i in range(max(0, n)) for _ in range(f)]
