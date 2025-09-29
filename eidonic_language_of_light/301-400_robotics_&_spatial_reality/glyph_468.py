# glyph_468.py — Safe Rollback
# -----------------------------------------------------------------------------
# ID:            468
# Pack:          Pack 005 (401–500)
# Name:          Safe Rollback
# Class:         recovery
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_468(state: Mapping[str, Any], snapshot: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Safe Rollback — restore state to a known-good snapshot.

    Overview
    --------
    Returns a copy of `snapshot`, ignoring extra keys in `state`.

    Parameters
    ----------
    state    : Mapping[str,Any]
    snapshot : Mapping[str,Any]

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_468({"a":1,"b":2}, {"a":0})
    {'a': 0}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(k)
    """
    return dict(snapshot)
