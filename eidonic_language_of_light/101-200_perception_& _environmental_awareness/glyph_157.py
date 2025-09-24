# glyph_157.py — Quantum Cascade Definer
# -----------------------------------------------------------------------------
# ID:            157
# Pack:          Pack 002 (101–200)
# Name:          Quantum Cascade Definer
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from collections import Counter
from typing import Sequence, List, Tuple

def glyph_157(seq: Sequence[int]) -> List[Tuple[int, int]]:
    """
    Quantum Cascade Definer — run-length encode an integer sequence.

    Overview
    --------
    Returns [(value, count), ...] for consecutive equal values.

    Parameters
    ----------
    seq : Sequence[int]

    Returns
    -------
    List[Tuple[int,int]]
        RLE pairs.

    Examples
    --------
    >>> glyph_157([1,1,2,2,2,1])
    [(1, 2), (2, 3), (1, 1)]
    """
    if not seq: return []
    out=[]; cur=seq[0]; cnt=1
    for v in seq[1:]:
        if v==cur: cnt+=1
        else: out.append((int(cur), cnt)); cur=v; cnt=1
    out.append((int(cur), cnt))
    return out
