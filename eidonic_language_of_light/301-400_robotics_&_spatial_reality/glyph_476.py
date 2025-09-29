# glyph_476.py — Fault Oracle
# -----------------------------------------------------------------------------
# ID:            476
# Pack:          Pack 005 (401–500)
# Name:          Fault Oracle
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_476(counters: Mapping[str, int], *, thresholds: Mapping[str, int]) -> Dict[str, bool]:
    """
    Fault Oracle — per-metric breach flags.

    Overview
    --------
    Returns a map {metric: True/False} where True indicates counter >= threshold.

    Parameters
    ----------
    counters   : Mapping[str,int]
    thresholds : Mapping[str,int]

    Returns
    -------
    Dict[str,bool]

    Examples
    --------
    >>> glyph_476({"err":5}, thresholds={"err":3})
    {'err': True}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(k)
    """
    out: Dict[str, bool] = {}
    for k, v in counters.items():
        out[k] = int(v) >= int(thresholds.get(k, 0))
    for k in thresholds:
        out.setdefault(k, False)
    return out
