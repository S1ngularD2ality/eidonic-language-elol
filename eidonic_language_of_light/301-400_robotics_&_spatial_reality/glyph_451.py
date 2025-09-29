# glyph_451.py — Shared Scratch
# -----------------------------------------------------------------------------
# ID:            451
# Pack:          Pack 005 (401–500)
# Name:          Shared Scratch
# Class:         state_manager
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_451(scratch: Mapping[str, Any], key: str, value: Any) -> Dict[str, Any]:
    """
    Shared Scratch — immutable write to a shared temp dict.

    Overview
    --------
    Returns a shallow-copied dict with `key` set to `value`.

    Parameters
    ----------
    scratch : Mapping[str,Any]
    key     : str
    value   : Any

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_451({}, "tmp", 42)["tmp"]
    42

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(n)
    """
    out = dict(scratch)
    out[str(key)] = value
    return out
