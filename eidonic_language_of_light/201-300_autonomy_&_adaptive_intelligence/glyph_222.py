# glyph_222.py — Harmonic Gate Duplicator
# -----------------------------------------------------------------------------
# ID:            222
# Pack:          Pack 003 (201–300)
# Name:          Harmonic Gate Duplicator
# Class:         generator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, TypeVar

T = TypeVar("T")

def glyph_222(seq: Sequence[T], *, factor: int = 2) -> List[T]:
    """
    Harmonic Gate Duplicator — repeat each element `factor` times.

    Overview
    --------
    Deterministic upsampling by integer replication; preserves order.

    Parameters
    ----------
    seq : Sequence[T]
    factor : int, optional (default: 2)

    Returns
    -------
    List[T]
        Duplicated sequence.

    Examples
    --------
    >>> glyph_222([1,2,3], factor=3)
    [1,1,1,2,2,2,3,3,3]

    Exceptions
    ----------
    - ValueError : if factor < 1.

    Complexity
    ----------
    - Time  : O(n·factor)
    - Space : O(n·factor)
    """
    f = int(factor)
    if f < 1:
        raise ValueError("factor must be >= 1")
    return [v for v in seq for _ in range(f)]
