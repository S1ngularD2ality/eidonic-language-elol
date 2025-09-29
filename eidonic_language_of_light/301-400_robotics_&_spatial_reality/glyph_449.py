# glyph_449.py — Memory Lease
# -----------------------------------------------------------------------------
# ID:            449
# Pack:          Pack 005 (401–500)
# Name:          Memory Lease
# Class:         memory
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_449(state: Mapping[str, Any], key: str, value: Any, *, ttl: int) -> Dict[str, Any]:
    """
    Memory Lease — set a value with a time-to-live counter (decrement external).

    Overview
    --------
    Stores {'value': value, 'ttl': ttl}; does not tick—external scheduler decrements.

    Parameters
    ----------
    state : Mapping[str,Any]
    key   : str
    value : Any
    ttl   : int

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_449({}, "k", 1, ttl=3)["k"]["ttl"]
    3

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    out = dict(state)
    out[str(key)] = {"value": value, "ttl": int(ttl)}
    return out
