# glyph_494.py — Outbox Queue
# -----------------------------------------------------------------------------
# ID:            494
# Pack:          Pack 005 (401–500)
# Name:          Outbox Queue
# Class:         queue
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, List, Dict

def glyph_494(outbox: List[Mapping[str, Any]], msg: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Outbox Queue — enqueue a message immutably.

    Overview
    --------
    Returns {'outbox': new_list, 'size': len}.

    Parameters
    ----------
    outbox : List[Mapping[str,Any]]
    msg    : Mapping[str,Any]

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_494([], {'m':1})['size']
    1

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    q = list(outbox)
    q.append(dict(msg))
    return {"outbox": q, "size": len(q)}
