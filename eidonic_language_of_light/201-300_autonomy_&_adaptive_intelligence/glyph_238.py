# glyph_238.py — Phase Collapse Distributor
# -----------------------------------------------------------------------------
# ID:            238
# Pack:          Pack 003 (201–300)
# Name:          Phase Collapse Distributor
# Class:         combinator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_238(seq: Sequence[int], *, lanes: int = 2) -> List[List[int]]:
    """
    Phase Collapse Distributor — partition by index modulo `lanes`.

    Overview
    --------
    Splits a stream into parallel lanes preserving intra-lane order.

    Parameters
    ----------
    seq : Sequence[int]
    lanes : int, optional (default: 2)

    Returns
    -------
    List[List[int]]
        Lanes (length == lanes).
    """
    L = max(1, int(lanes))
    out = [[] for _ in range(L)]
    for i, v in enumerate(seq):
        out[i % L].append(int(v))
    return out
