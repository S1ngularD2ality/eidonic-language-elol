# glyph_522.py — Deep Log Scan
# -----------------------------------------------------------------------------
# ID:            522
# Pack:          Pack 006 (501–600)
# Name:          Deep Log Scan
# Class:         logging_auditing
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # pure scanning; no I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Mapping, Any, List, Dict

def glyph_522(entries: Sequence[Mapping[str, Any]],
              *,
              contains: Sequence[str] = (),
              min_severity: int = 0) -> List[Dict[str, Any]]:
    """
    Deep Log Scan — filter audit entries by substrings and severity.

    Overview
    --------
    Select entries whose canonicalized 'msg' contains all tokens in `contains`
    and whose integer 'sev' meets or exceeds `min_severity`.

    Parameters
    ----------
    entries      : Sequence[Mapping[str,Any]]
    contains     : Sequence[str]
    min_severity : int

    Returns
    -------
    List[Dict[str,Any]]

    Examples
    --------
    >>> logs = [{'msg':'failed login for a','sev':3},{'msg':'ok','sev':1}]
    >>> glyph_522(logs, contains=['failed','login'], min_severity=2)[0]['sev']
    3

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n·m)  (tokens × entries)
    - Space : O(k)
    """
    needles = [s.lower() for s in contains]
    out: List[Dict[str, Any]] = []
    for e in entries:
        msg = str(e.get("msg", "")).lower()
        sev = int(e.get("sev", 0))
        if sev >= min_severity and all(t in msg for t in needles):
            out.append(dict(e))
    return out
