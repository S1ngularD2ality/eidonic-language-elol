# glyph_131.py — Inner Lens Distributor
# -----------------------------------------------------------------------------
# ID:            131
# Pack:          Pack 002 (101–200)
# Name:          Inner Lens Distributor
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_131(seq: Sequence[int], *, lenses: int) -> List[List[int]]:
    """
    Inner Lens Distributor — dispatch indices into `lenses` channels.

    Overview
    --------
    Channel i receives items where index % lenses == i.

    Parameters
    ----------
    seq : Sequence[int]
    lenses : int

    Returns
    -------
    List[List[int]]
        Channelized indices.
    """
    if lenses < 1:
        return []
    out: List[List[int]] = [[] for _ in range(lenses)]
    for i, v in enumerate(seq):
        out[i % lenses].append(int(v))
    return out
