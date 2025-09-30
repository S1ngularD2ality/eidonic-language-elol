# glyph_519.py — Access Logger
# -----------------------------------------------------------------------------
# ID:            519
# Pack:          Pack 006 (501–600)
# Name:          Access Logger
# Class:         logging_auditing
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # append-only in-memory
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, List, Dict

def glyph_519(log: List[Mapping[str, Any]], entry: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Access Logger — append immutable audit entry with index.

    Overview
    --------
    Returns {'log': new_log, 'index': idx}.

    Parameters
    ----------
    log   : List[Mapping[str,Any]]
    entry : Mapping[str,Any]

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_519([], {'actor':'a','action':'read'})['index']
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
