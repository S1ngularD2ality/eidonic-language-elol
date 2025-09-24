# glyph_226.py — Mirror Cascade Filter
# -----------------------------------------------------------------------------
# ID:            226
# Pack:          Pack 003 (201–300)
# Name:          Mirror Cascade Filter
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_226(seq: Sequence[float], *, passes: int = 2) -> List[float]:
    """
    Mirror Cascade Filter — alternating smooth & mirror-enforce passes.

    Overview
    --------
    Repeats: 3-point mean filter with reflection padding, then average with reverse.

    Parameters
    ----------
    seq : Sequence[float]
    passes : int, optional (default: 2)

    Returns
    -------
    List[float]
        Filtered sequence.

    Examples
    --------
    >>> glyph_226([0,10,0,10,0], passes=1)  # doctest: +ELLIPSIS
    [...]
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0: return []
    k = 1
    for _ in range(max(0, passes)):
        # mean filter (window=3) with reflection
        pad = x[k:0:-1] + x + x[-2:-k-2:-1] if n > 1 else x*(2*k+1)
        y = []
        for i in range(n):
            w = pad[i:i+2*k+1]
            y.append(sum(w)/len(w))
        # mirror enforce
        x = [(y[i] + y[n-1-i]) * 0.5 for i in range(n)]
    return x
