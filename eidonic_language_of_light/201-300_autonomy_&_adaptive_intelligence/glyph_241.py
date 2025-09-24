# glyph_241.py — Mirror Trail Inverter
# -----------------------------------------------------------------------------
# ID:            241
# Pack:          Pack 003 (201–300)
# Name:          Mirror Trail Inverter
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_241(seq: Sequence[float]) -> Tuple[List[float], List[float]]:
    """
    Mirror Trail Inverter — produce forward and inverted mirror trails.

    Overview
    --------
    Returns (mean_with_reverse, delta_from_reverse). The first is the palindromized
    average; the second is x - reverse(x).

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], List[float])
        (mirror_mean, mirror_delta)

    Examples
    --------
    >>> m, d = glyph_241([1,2,3,4])
    >>> m, d
    ([2.5, 2.5, 2.5, 2.5], [-3.0, -1.0, 1.0, 3.0])

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    x = [float(v) for v in seq]
    n = len(x)
    rev = x[::-1]
    mean = [(x[i] + rev[i]) * 0.5 for i in range(n)]
    delta = [x[i] - rev[i] for i in range(n)]
    return mean, delta
