# glyph_438.py — Episode Writer
# -----------------------------------------------------------------------------
# ID:            438
# Pack:          Pack 005 (401–500)
# Name:          Episode Writer
# Class:         writer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict, List

def glyph_438(state: Mapping[str, Any], event: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Episode Writer — immutably append an event.

    Overview
    --------
    Copies state, appends event to 'events', and sets 'last'.

    Parameters
    ----------
    state : Mapping[str,Any]
    event : Mapping[str,Any]

    Returns
    -------
    Dict[str, Any]

    Examples
    --------
    >>> glyph_438({"events":[]}, {"type":"tick"})["last"]["type"]
    'tick'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)  (copy of list)
    - Space : O(n)
    """
    out = dict(state)
    evs: List[Mapping[str,Any]] = list(out.get("events", []))
    evs.append(dict(event))
    out["events"] = evs
    out["last"] = dict(event)
    return out
