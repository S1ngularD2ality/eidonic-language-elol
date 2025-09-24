# glyph_034.py — Flame Cascade Sorter
# -----------------------------------------------------------------------------
# ID:            034
# Pack:          Pack 001 (000–100)
# Name:          Flame Cascade Sorter
# Class:         control
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_034(seq: Sequence[float], *, descending: bool = False) -> List[float]:
    """
    Flame Cascade Sorter — stable sort with optional descending order.

    Overview
    --------
    Returns a new list sorted by value; preserves relative order of equals.

    Parameters
    ----------
    seq : Sequence[float]
    descending : bool, optional (default: False)

    Returns
    -------
    List[float]
        Sorted sequence.
    """
    return sorted([float(v) for v in seq], reverse=bool(descending))
