# glyph_497.py — Partition Bridge
# -----------------------------------------------------------------------------
# ID:            497
# Pack:          Pack 005 (401–500)
# Name:          Partition Bridge
# Class:         reconciler
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping, Any, Dict

def glyph_497(left: Sequence[Mapping[str, Any]], right: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    """
    Partition Bridge — symmetric difference of two event streams by 'id'.

    Overview
    --------
    Emits {'only_left':[...],'only_right':[...]} with elements as dicts.

    Parameters
    ----------
    left  : Sequence[Mapping[str,Any]]
    right : Sequence[Mapping[str,Any]]

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_497([{'id':1}], [{'id':2}])['only_right'][0]['id']
    2

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n + m)
    - Space : O(n + m)
    """
    by_id_l = {e.get("id"): dict(e) for e in left}
    by_id_r = {e.get("id"): dict(e) for e in right}
    only_l = [by_id_l[k] for k in by_id_l.keys() - by_id_r.keys()]
    only_r = [by_id_r[k] for k in by_id_r.keys() - by_id_l.keys()]
    return {"only_left": only_l, "only_right": only_r}
