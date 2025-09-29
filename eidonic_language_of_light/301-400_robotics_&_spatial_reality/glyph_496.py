# glyph_495.py — Inflight Ledger
# -----------------------------------------------------------------------------
# ID:            495
# Pack:          Pack 005 (401–500)
# Name:          Inflight Ledger
# Class:         tracker
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_495(ledger: Mapping[str, Any], packet_id: str, *, action: str) -> Dict[str, Any]:
    """
    Inflight Ledger — add/remove packet ids from an inflight set.

    Overview
    --------
    action ∈ {'add','ack'}; returns new dict with 'inflight' list updated.

    Parameters
    ----------
    ledger    : Mapping[str,Any]
    packet_id : str
    action    : str

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_495({'inflight':[]}, 'p1', action='add')['inflight']
    ['p1']

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)  (copy)
    - Space : O(n)
    """
    inflight = list(ledger.get("inflight", []))
    if action == "add":
        if packet_id not in inflight:
            inflight.append(packet_id)
    elif action == "ack":
        if packet_id in inflight:
            inflight.remove(packet_id)
    out = dict(ledger)
    out["inflight"] = inflight
    return out
