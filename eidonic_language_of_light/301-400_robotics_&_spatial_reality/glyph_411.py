# glyph_411.py — Skill Broker
# -----------------------------------------------------------------------------
# ID:            411
# Pack:          Pack 005 (401–500)
# Name:          Skill Broker
# Class:         matcher
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Optional

def glyph_411(task_reqs: Mapping[str, bool], agents_caps: Mapping[str, Mapping[str, bool]]) -> Optional[str]:
    """
    Skill Broker — select first agent satisfying all required capabilities.

    Overview
    --------
    Extracts required capability names (True in task_reqs) and returns the first
    agent whose capability set is a superset.

    Parameters
    ----------
    task_reqs   : Mapping[str,bool]
    agents_caps : Mapping[str, Mapping[str,bool]]

    Returns
    -------
    Optional[str] : agent_id or None if unsatisfied.

    Examples
    --------
    >>> glyph_411({"see":True}, {"a":{"see":True}, "b":{"see":False}})
    'a'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(A·C)
    - Space : O(C)
    """
    req = {k for k, v in task_reqs.items() if v}
    for aid, caps in agents_caps.items():
        if req.issubset({k for k, v in caps.items() if v}):
            return aid
    return None
