# glyph_484.py — Accord Replay
# -----------------------------------------------------------------------------
# ID:            484
# Pack:          Pack 005 (401–500)
# Name:          Accord Replay
# Class:         simulator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping, Any, List, Dict

def glyph_484(events: Sequence[Mapping[str, Any]], state0: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Accord Replay — fold events over initial state using 'op' semantics.

    Overview
    --------
    Supports ops: 'set' → state[k]=v; 'inc' → state[k]+=v; 'del' → delete k.

    Parameters
    ----------
    events : Sequence[{'op':str,'key':str,'value':Any}]
    state0 : Mapping[str,Any]

    Returns
    -------
    Dict[str,Any] : final state

    Examples
    --------
    >>> glyph_484([{'op':'set','key':'x','value':1}], {})
    {'x': 1}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    s: Dict[str, Any] = dict(state0)
    for e in events:
        op = str(e.get("op", ""))
        k = str(e.get("key", ""))
        v = e.get("value", None)
        if op == "set":
            s[k] = v
        elif op == "inc":
            s[k] = s.get(k, 0) + v
        elif op == "del":
            s.pop(k, None)
    return s
