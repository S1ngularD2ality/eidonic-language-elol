# glyph_493.py — Packet Journal
# -----------------------------------------------------------------------------
# ID:            493
# Pack:          Pack 005 (401–500)
# Name:          Packet Journal
# Class:         log
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, List, Dict

def glyph_493(log: List[Mapping[str, Any]], packet: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Packet Journal — append packet with deterministic monotonic index.

    Overview
    --------
    Returns {'log': new_log, 'index': idx}.

    Parameters
    ----------
    log    : List[Mapping[str,Any]]
    packet : Mapping[str,Any]

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_493([], {'id':1})['index']
    0

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    new_log = list(log)
    new_log.append(dict(packet))
    return {"log": new_log, "index": len(new_log) - 1}
