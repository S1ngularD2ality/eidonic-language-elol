# glyph_074.py — Mirror Logic Shuffler
# -----------------------------------------------------------------------------
# ID:            074
# Pack:          Pack 001 (000–100)
# Name:          Mirror Logic Shuffler
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import random
from typing import Sequence, List, TypeVar

T = TypeVar("T")

def glyph_074(seq: Sequence[T], *, seed: int | None = None) -> List[T]:
    """
    Mirror Logic Shuffler — reproducible permutation.

    Overview
    --------
    Returns a shuffled copy of `seq`. If `seed` is provided, the permutation is
    deterministic for that seed.

    Parameters
    ----------
    seq : Sequence[T]
    seed : int | None, optional

    Returns
    -------
    List[T]
        Shuffled sequence.

    Examples
    --------
    >>> glyph_074([1,2,3], seed=0)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    r = random.Random(seed)
    out = list(seq)
    r.shuffle(out)
    return out
