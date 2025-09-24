# glyph_290.py — Symbol Thread Multiplier
# -----------------------------------------------------------------------------
# ID:            290
# Pack:          Pack 003 (201–300)
# Name:          Symbol Thread Multiplier
# Class:         generator
# Stability:     Stable
# Version:       1.0.2
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_290(seq: Sequence[str], *, factor: int = 2) -> List[str]:
    """
    Symbol Thread Multiplier — repeat tokens `factor` times.

    Overview
    --------
    Preserves order; deterministic.

    Parameters
    ----------
    seq : Sequence[str]
    factor : int, optional (default: 2)

    Returns
    -------
    List[str]
        Multiplied sequence.

    Examples
    --------
    >>> glyph_290(["a","b"], factor=3)
    ['a','a','a','b','b','b']

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n·factor)
    - Space : O(n·factor)
    """
    f = max(1, int(factor))
    return [s for s in seq for _ in range(f)]
