# glyph_439.py — Episode Reader
# -----------------------------------------------------------------------------
# ID:            439
# Pack:          Pack 005 (401–500)
# Name:          Episode Reader
# Class:         reader
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, List

def glyph_439(state: Mapping[str, Any], *, last_k: int = 1) -> List[Mapping[str, Any]]:
    """
    Episode Reader — return the last K events.

    Overview
    --------
    Non-destructive slice of the trailing events.

    Parameters
    ----------
    state  : Mapping[str,Any]
    last_k : int, optional (default: 1)

    Returns
    -------
    List[Mapping[str,Any]]

    Examples
    --------
    >>> glyph_439({"events":[{"id":1},{"id":2},{"id":3}]}, last_k=2)
    [{'id': 2}, {'id': 3}]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(k)
    """
    evs = list(state.get("events", []))
    if last_k <= 0:
        return []
    return [dict(e) for e in evs[-last_k:]]
