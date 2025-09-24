# glyph_233.py — Liminal Gate Condenser
# -----------------------------------------------------------------------------
# ID:            233
# Pack:          Pack 003 (201–300)
# Name:          Liminal Gate Condenser
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_233(seq: Sequence[float]) -> float:
    """
    Liminal Gate Condenser — compute robust (trimmed) mean.

    Overview
    --------
    Drops the min and max (if available) and averages the rest.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    float
        Condensed average.

    Examples
    --------
    >>> glyph_233([0, 100, 1, 2])
    1.5
    """
    x = [float(v) for v in seq]
    if len(x) <= 2:
        return sum(x)/len(x) if x else 0.0
    x.sort()
    core = x[1:-1]
    return sum(core)/len(core)
