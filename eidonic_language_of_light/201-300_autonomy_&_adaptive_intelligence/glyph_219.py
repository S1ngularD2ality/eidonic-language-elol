# glyph_219.py — Spiral Dream Binder
# -----------------------------------------------------------------------------
# ID:            219
# Pack:          Pack 003 (201–300)
# Name:          Spiral Dream Binder
# Class:         combinator
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_219(a: Sequence[int], b: Sequence[int]) -> List[int]:
    """
    Spiral Dream Binder — weave two sequences alternately (A|B).

    Overview
    --------
    Emits [a0, b0, a1, b1, ...] up to min lengths, then appends the remainder.

    Parameters
    ----------
    a : Sequence[int]
    b : Sequence[int]

    Returns
    -------
    List[int]
        Bound sequence.

    Examples
    --------
    >>> glyph_219([1,2,3],[9,8])
    [1, 9, 2, 8, 3]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(len(a)+len(b))
    - Space : O(len(a)+len(b))
    """
    out: List[int] = []
    m = min(len(a), len(b))
    for i in range(m):
        out.append(int(a[i])); out.append(int(b[i]))
    tail = a[m:] if len(a) > m else b[m:]
    out += [int(v) for v in tail]
    return out
