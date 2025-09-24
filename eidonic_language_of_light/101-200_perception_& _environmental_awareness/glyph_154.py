# glyph_154.py — Spiral Flame Distributor
# -----------------------------------------------------------------------------
# ID:            154
# Pack:          Pack 002 (101–200)
# Name:          Spiral Flame Distributor
# Class:         combinator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_154(seq: Sequence[int], *, turns: int = 2) -> List[List[int]]:
    """
    Spiral Flame Distributor — distribute items across spiral turns.

    Overview
    --------
    Splits the sequence into `turns` lists by index modulo `turns`.

    Parameters
    ----------
    seq : Sequence[int]
    turns : int, optional (default: 2)

    Returns
    -------
    List[List[int]]
        Buckets per turn.

    Examples
    --------
    >>> glyph_154([0,1,2,3,4], turns=2)
    [[0, 2, 4], [1, 3]]
    """
    t = max(1, int(turns))
    out = [[] for _ in range(t)]
    for i, v in enumerate(seq):
        out[i % t].append(int(v))
    return out
