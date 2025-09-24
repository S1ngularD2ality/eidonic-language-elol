# glyph_051.py — Subdimensional Key Splitter
# -----------------------------------------------------------------------------
# ID:            051
# Pack:          Pack 001 (000–100)
# Name:          Subdimensional Key Splitter
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_051(seq: Sequence[float], *, keys: int) -> List[List[float]]:
    """
    Subdimensional Key Splitter — partition by index modulo classes.

    Overview
    --------
    Splits `seq` into `keys` streams by `i mod keys`. Use to demultiplex periodic roles.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.
    keys : int
        Number of modulo classes (>= 1).

    Returns
    -------
    List[List[float]]
        `keys` subsequences preserving original order per class.

    Examples
    --------
    >>> glyph_051([0,1,2,3,4], keys=2)
    [[0,2,4],[1,3]]

    Exceptions
    ----------
    - ValueError : if `keys < 1`.

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if keys < 1:
        raise ValueError("keys must be >= 1")
    out: List[List[float]] = [[] for _ in range(keys)]
    for i, v in enumerate(seq):
        out[i % keys].append(float(v))
    return out
