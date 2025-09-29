# glyph_485.py — Mesh Beacon
# -----------------------------------------------------------------------------
# ID:            485
# Pack:          Pack 005 (401–500)
# Name:          Mesh Beacon
# Class:         broadcaster
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, List

def glyph_485(node_id: str, payload: Mapping[str, Any], neighbors: List[str]) -> List[str]:
    """
    Mesh Beacon — craft broadcast frames to immediate neighbors.

    Overview
    --------
    Emits strings like "from=node_id|to=peer|json=<...>" deterministically.

    Parameters
    ----------
    node_id   : str
    payload   : Mapping[str,Any]
    neighbors : List[str]

    Returns
    -------
    List[str] : frames (one per neighbor)

    Examples
    --------
    >>> frames = glyph_485("A", {"hello":1}, ["B","C"]); len(frames)
    2

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(d)
    - Space : O(d)
    """
    import json
    data = json.dumps(dict(payload), sort_keys=True)
    return [f"from={node_id}|to={p}|json={data}" for p in neighbors]
