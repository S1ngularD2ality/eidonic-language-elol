# glyph_182.py — Anchor Lens Reducer
# -----------------------------------------------------------------------------
# ID:            182
# Pack:          Pack 002 (101–200)
# Name:          Anchor Lens Reducer
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_182(field: Sequence[Sequence[float]], *, window: int = 2) -> List[float]:
    """
    Anchor Lens Reducer — pooled row features via average pooling.

    Overview
    --------
    For each row, pools contiguous windows of width `window` and averages them,
    then averages all pools to produce a single value per row.

    Parameters
    ----------
    field : Sequence[Sequence[float]]
    window : int, optional (default: 2)

    Returns
    -------
    List[float]
        One pooled value per row.

    Examples
    --------
    >>> glyph_182([[1,2,3,4],[5,6,7,8]], window=2)
    [2.5, 6.5]

    Exceptions
    ----------
    - ValueError : if window < 1.

    Complexity
    ----------
    - Time  : O(H·W)
    - Space : O(H)
    """
    if window < 1:
        raise ValueError("window must be >= 1")
    out: List[float] = []
    for row in field:
        r = [float(v) for v in row]
        if not r:
            out.append(0.0); continue
        pools = []
        for i in range(0, len(r), window):
            pools.append(sum(r[i:i+window]) / max(1, len(r[i:i+window])))
        out.append(sum(pools) / len(pools))
    return out
