# glyph_477.py — Dispute Mediator
# -----------------------------------------------------------------------------
# ID:            477
# Pack:          Pack 005 (401–500)
# Name:          Dispute Mediator
# Class:         mediator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_477(a: Mapping[str, Any], b: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Dispute Mediator — reconcile two dicts by rule: agree → keep, disagree → list.

    Overview
    --------
    Emits {key: value} when equal; else {key: [a_value, b_value]}.

    Parameters
    ----------
    a : Mapping[str,Any]
    b : Mapping[str,Any]

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_477({"x":1,"y":2}, {"x":1,"y":3})
    {'x': 1, 'y': [2, 3]}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(k)
    """
    keys = set(a) | set(b)
    out: Dict[str, Any] = {}
    for k in keys:
        av, bv = a.get(k), b.get(k)
        out[k] = av if av == bv else [av, bv]
    return out
