# glyph_454.py — Handoff Switchboard
# -----------------------------------------------------------------------------
# ID:            454
# Pack:          Pack 005 (401–500)
# Name:          Handoff Switchboard
# Class:         router
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping

def glyph_454(status: Mapping[str, float], routes: Mapping[str, str], *, busy_threshold: float = 0.8) -> str:
    """
    Handoff Switchboard — route to least-busy eligible agent.

    Overview
    --------
    Filters out agents with load ≥ busy_threshold; picks lowest-load remainder.

    Parameters
    ----------
    status         : Mapping[str,float] — agent_id → load [0..1]
    routes         : Mapping[str,str]   — optional allowlist; empty means all
    busy_threshold : float, optional (default: 0.8)

    Returns
    -------
    str : selected agent_id or '' if none available.

    Examples
    --------
    >>> glyph_454({"a":0.2,"b":0.9}, {}, busy_threshold=0.8)
    'a'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    allow = set(routes.values()) if routes else set(status.keys())
    candidates = [(aid, load) for aid, load in status.items() if aid in allow and float(load) < float(busy_threshold)]
    if not candidates:
        return ""
    return min(candidates, key=lambda kv: float(kv[1]))[0]
