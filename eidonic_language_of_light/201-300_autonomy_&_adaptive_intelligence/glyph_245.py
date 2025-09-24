# glyph_245.py — Timeline Key Mapper
# -----------------------------------------------------------------------------
# ID:            245
# Pack:          Pack 003 (201–300)
# Name:          Timeline Key Mapper
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Dict

def glyph_245(seq: Sequence[int], *, phases: int) -> Dict[int, list[int]]:
    """
    Timeline Key Mapper — bucket indices by phase key.

    Overview
    --------
    Groups positions i by i % phases.

    Parameters
    ----------
    seq : Sequence[int]
    phases : int

    Returns
    -------
    Dict[int, list[int]]
        phase_key -> indices

    Examples
    --------
    >>> glyph_245(range(7), phases=3)
    {0:[0,3,6], 1:[1,4], 2:[2,5]}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    p = max(1, int(phases))
    out: Dict[int, list[int]] = {k: [] for k in range(p)}
    for i, _ in enumerate(seq):
        out[i % p].append(i)
    return out
