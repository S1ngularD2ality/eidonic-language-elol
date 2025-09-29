# glyph_488.py — Hop Relay
# -----------------------------------------------------------------------------
# ID:            488
# Pack:          Pack 005 (401–500)
# Name:          Hop Relay
# Class:         router
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_488(path: list[str], *, ttl: int) -> list[str]:
    """
    Hop Relay — pop the current hop and decrement TTL.

    Overview
    --------
    Returns remaining path if ttl>0 and path not empty; else [].

    Parameters
    ----------
    path : list[str]
    ttl  : int

    Returns
    -------
    list[str]

    Examples
    --------
    >>> glyph_488(['A','B','C'], ttl=2)
    ['B', 'C']

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if ttl <= 0 or not path:
        return []
    return path[1:]
