# glyph_469.py — Soft Vote
# -----------------------------------------------------------------------------
# ID:            469
# Pack:          Pack 005 (401–500)
# Name:          Soft Vote
# Class:         consensus
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping

def glyph_469(weights: Mapping[str, float]) -> str:
    """
    Soft Vote — argmax over weighted options.

    Overview
    --------
    Returns the option with highest weight; ties broken by name.

    Parameters
    ----------
    weights : Mapping[option, weight]

    Returns
    -------
    str

    Examples
    --------
    >>> glyph_469({"A":0.3,"B":0.7})
    'B'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    if not weights:
        return ""
    return min((-float(v), str(k)) for k, v in weights.items())[1]
