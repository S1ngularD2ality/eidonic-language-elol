# glyph_420.py — Text-to-Vision Aligner
# -----------------------------------------------------------------------------
# ID:            420
# Pack:          Pack 005 (401–500)
# Name:          Text-to-Vision Aligner
# Class:         aligner
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_420(tokens: Sequence[str], regions: Sequence[str]) -> List[int]:
    """
    Text-to-Vision Aligner — greedy bipartite alignment by lexical overlap.

    Overview
    --------
    For each token, selects the first region whose lowercase label contains the token
    (or vice versa). If none match, emits -1.

    Parameters
    ----------
    tokens  : Sequence[str]
    regions : Sequence[str]

    Returns
    -------
    List[int] : region indices per token.

    Examples
    --------
    >>> glyph_420(["red","car"], ["car.1","tree"])
    [0, 0]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(T·R)
    - Space : O(1)
    """
    out: List[int] = []
    low_regs = [r.lower() for r in regions]
    for t in tokens:
        lt = t.lower()
        idx = -1
        for j, r in enumerate(low_regs):
            if lt in r or r in lt:
                idx = j
                break
        out.append(idx)
    return out
