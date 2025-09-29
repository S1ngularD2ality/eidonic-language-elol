# glyph_478.py — Commit Log
# -----------------------------------------------------------------------------
# ID:            478
# Pack:          Pack 005 (401–500)
# Name:          Commit Log
# Class:         log
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, List, Dict

def glyph_478(log: List[Mapping[str, Any]], entry: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Commit Log — append immutable entry with monotonic index.

    Overview
    --------
    Returns {'log': new_log, 'index': idx} where idx is the entry's position.

    Parameters
    ----------
    log   : List[Mapping[str,Any]]
    entry : Mapping[str,Any]

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_478([], {"op":"set"})['index']
    0

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)  (copy)
    - Space : O(n)
    """
    new_log = list(log)
    new_log.append(dict(entry))
    return {"log": new_log, "index": len(new_log) - 1}
