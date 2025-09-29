# glyph_491.py — TTL Guardian
# -----------------------------------------------------------------------------
# ID:            491
# Pack:          Pack 005 (401–500)
# Name:          TTL Guardian
# Class:         guard
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_491(ttl: int) -> int:
    """
    TTL Guardian — clamp TTL to non-negative and decrement by 1 if > 0.

    Overview
    --------
    Returns max(ttl-1, 0).

    Parameters
    ----------
    ttl : int

    Returns
    -------
    int

    Examples
    --------
    >>> glyph_491(3)
    2

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    return max(0, int(ttl) - 1)
