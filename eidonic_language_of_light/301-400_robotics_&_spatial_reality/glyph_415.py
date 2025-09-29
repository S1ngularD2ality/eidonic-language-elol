# glyph_415.py — Consent Gate
# -----------------------------------------------------------------------------
# ID:            415
# Pack:          Pack 005 (401–500)
# Name:          Consent Gate
# Class:         gate
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping

def glyph_415(policy: Mapping[str, bool], request: Mapping[str, str]) -> bool:
    """
    Consent Gate — allow if policy[action] is True, else deny.

    Overview
    --------
    Looks up the requested 'action' in policy; absent keys are treated as False.

    Parameters
    ----------
    policy  : Mapping[str,bool]
    request : Mapping[str,str]  (expects 'action')

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_415({"write":False,"read":True}, {"action":"read"})
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    return bool(policy.get(str(request.get("action", "")), False))
