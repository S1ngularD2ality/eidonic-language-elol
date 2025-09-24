# glyph_202.py — Dream Mirror Collapser
# -----------------------------------------------------------------------------
# ID:            202
# Pack:          Pack 003 (201–300)
# Name:          Dream Mirror Collapser
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_202(seq: Sequence[float]) -> Tuple[List[float], float]:
    """
    Dream Mirror Collapser — collapse a sequence into its mirror-consistent core.

    Overview
    --------
    Returns the element-wise average of x and reversed(x) (palindromization) and
    the mean absolute deviation from that mirror.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], float)
        (mirror_collapsed, deviation)

    Examples
    --------
    >>> glyph_202([1,2,3,4])
    ([2.5, 2.5, 2.5, 2.5], 1.0)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0: return [], 0.0
    m = [(x[i] + x[n-1-i]) * 0.5 for i in range(n)]
    dev = sum(abs(x[i] - m[i]) for i in range(n)) / n
    return m, dev
