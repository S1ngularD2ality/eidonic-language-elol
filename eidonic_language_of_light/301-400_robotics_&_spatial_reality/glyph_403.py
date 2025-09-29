# glyph_403.py — Agent Birthright
# -----------------------------------------------------------------------------
# ID:            403
# Pack:          Pack 005 (401–500)
# Name:          Agent Birthright
# Class:         initializer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, Mapping, Any

def glyph_403(agent_id: str, seed_traits: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Agent Birthright — mint a minimal, deterministic agent profile.

    Overview
    --------
    Emits an immutable-ready dict containing ID, a shallow copy of traits, and an
    'active' flag.

    Parameters
    ----------
    agent_id    : str
    seed_traits : Mapping[str, Any]

    Returns
    -------
    Dict[str, Any] : {'id': str, 'traits': dict, 'active': True}

    Examples
    --------
    >>> glyph_403("alpha", {"courage":1})["active"]
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(k)
    """
    return {"id": str(agent_id), "traits": dict(seed_traits), "active": True}
