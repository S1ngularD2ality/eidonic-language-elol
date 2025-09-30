# glyph_532.py — Auth Log
# -----------------------------------------------------------------------------
# ID:            532
# Pack:          Pack 006 (501–600)
# Name:          Auth Log
# Class:         logging_auditing
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # append-only copy
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json
from typing import List, Dict, Any

def glyph_532(log: List[Dict[str, Any]], entry: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Auth Log — append immutable entry with canonical key order.

    Overview
    --------
    Dumps/loads JSON with sorted keys to stabilize order; returns new list.

    Parameters
    ----------
    log   : List[Dict[str,Any]]
    entry : Dict[str,Any]

    Returns
    -------
    List[Dict[str,Any]]

    Examples
    --------
    >>> glyph_532([], {'actor':'a','sev':2})[0]['actor']
    'a'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n + |entry|)
    - Space : O(n)
    """
    new = list(log)
    entry_json = json.dumps(dict(entry), sort_keys=True, separators=(",", ":"))
    new.append(json.loads(entry_json))
    return new
