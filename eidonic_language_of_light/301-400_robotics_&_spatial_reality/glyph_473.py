# glyph_473.py — CRDT Merge
# -----------------------------------------------------------------------------
# ID:            473
# Pack:          Pack 005 (401–500)
# Name:          CRDT Merge
# Class:         merger
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_473(l: Mapping[str, Any], r: Mapping[str, Any]) -> Dict[str, Any]:
    """
    CRDT Merge — last-writer-wins by 'ts' (timestamp float), per key.

    Overview
    --------
    For each key, choose value from side with larger 'ts'; missing 'ts' treated as 0.

    Parameters
    ----------
    l : Mapping[str,Any]
    r : Mapping[str,Any]

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_473({'a':{'v':1,'ts':1.0}}, {'a':{'v':2,'ts':2.0}})['a']['v']
    2

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(k)
    """
    keys = set(l) | set(r)
    out: Dict[str, Any] = {}
    for k in keys:
        lv, rv = l.get(k), r.get(k)
        lts = float(lv.get('ts', 0.0)) if isinstance(lv, dict) else 0.0
        rts = float(rv.get('ts', 0.0)) if isinstance(rv, dict) else 0.0
        out[k] = lv if lts >= rts else rv
    return out
