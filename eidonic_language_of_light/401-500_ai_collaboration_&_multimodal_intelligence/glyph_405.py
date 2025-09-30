# glyph_405.py — Intent Router
# -----------------------------------------------------------------------------
# ID:            405
# Pack:          Pack 005 (401–500)
# Name:          Intent Router
# Class:         router
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any

def glyph_405(message: Mapping[str, Any], routes: Mapping[str, str]) -> str:
    """
    Intent Router — choose a route by intent key with fallback.

    Overview
    --------
    Lowercases message['intent'] and looks up in routes; returns 'fallback' if missing.

    Parameters
    ----------
    message : Mapping[str, Any]  (expects 'intent': str)
    routes  : Mapping[str, str]  (intent → agent_id)

    Returns
    -------
    str : selected agent_id or 'fallback'

    Examples
    --------
    >>> glyph_405({"intent":"Search"}, {"search":"A"})
    'A'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    intent = str(message.get("intent", "")).lower()
    return routes.get(intent, "fallback")
