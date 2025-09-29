# glyph_429.py — Prompt Painter
# -----------------------------------------------------------------------------
# ID:            429
# Pack:          Pack 005 (401–500)
# Name:          Prompt Painter
# Class:         generator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping

def glyph_429(concepts: Mapping[str, float]) -> str:
    """
    Prompt Painter — render a stable, sorted prompt.

    Overview
    --------
    Sorts by key and prints "k:weight" with weight rounded to 3 decimals.

    Parameters
    ----------
    concepts : Mapping[str,float]

    Returns
    -------
    str

    Examples
    --------
    >>> glyph_429({"b":0.2,"a":1.0})
    'a:1.000, b:0.200'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k log k)
    - Space : O(k)
    """
    parts = [f"{k}:{round(float(v),3):.3f}" for k,v in sorted(concepts.items())]
    return ", ".join(parts)
