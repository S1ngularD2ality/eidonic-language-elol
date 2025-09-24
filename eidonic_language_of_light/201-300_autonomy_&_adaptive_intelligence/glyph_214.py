# glyph_214.py — Quantum Signal Binder
# -----------------------------------------------------------------------------
# ID:            214
# Pack:          Pack 003 (201–300)
# Name:          Quantum Signal Binder
# Class:         combinator
# Stability:     Stable
# Version:       1.0.1
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_214(a: Sequence[float], b: Sequence[float]) -> List[Tuple[float, float]]:
    """
    Quantum Signal Binder — zip two streams to entangled pairs.

    Overview
    --------
    Pairs elements up to min(len(a), len(b)) preserving order.

    Parameters
    ----------
    a : Sequence[float]
    b : Sequence[float]

    Returns
    -------
    List[Tuple[float, float]]
        Entangled pairs.

    Examples
    --------
    >>> glyph_214([1,2],[9,8,7])
    [(1.0, 9.0), (2.0, 8.0)]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(min(len(a),len(b)))
    - Space : O(min(len(a),len(b)))
    """
    m = min(len(a), len(b))
    return [(float(a[i]), float(b[i])) for i in range(m)]
