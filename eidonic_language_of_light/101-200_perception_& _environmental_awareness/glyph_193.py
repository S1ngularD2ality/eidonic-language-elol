# glyph_193.py — Anchor Flame Organizer
# -----------------------------------------------------------------------------
# ID:            193
# Pack:          Pack 002 (101–200)
# Name:          Anchor Flame Organizer
# Class:         combinator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_193(pairs: Sequence[Tuple[int, float]]) -> List[Tuple[int, float]]:
    """
    Anchor Flame Organizer — stable sort by anchor then value.

    Overview
    --------
    Sorts pairs (anchor, value) by ascending anchor, then by ascending value,
    preserving input order for ties.

    Parameters
    ----------
    pairs : Sequence[Tuple[int,float]]

    Returns
    -------
    List[Tuple[int,float]]
        Organized pairs.

    Examples
    --------
    >>> glyph_193([(2,1.0),(1,9.0),(1,3.0)])
    [(1, 3.0), (1, 9.0), (2, 1.0)]
    """
    return sorted(((int(a), float(v)) for a,v in pairs), key=lambda av: (av[0], av[1]))
