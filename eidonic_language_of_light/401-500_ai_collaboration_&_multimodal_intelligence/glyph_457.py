# glyph_457.py — Fallback Route
# -----------------------------------------------------------------------------
# ID:            457
# Pack:          Pack 005 (401–500)
# Name:          Fallback Route
# Class:         router
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_457(routes: Sequence[str], *, primary: int = 0) -> str:
    """
    Fallback Route — choose first non-empty route starting from primary, wrapping.

    Overview
    --------
    Scans circularly; returns '' if all are empty.

    Parameters
    ----------
    routes  : Sequence[str]
    primary : int, optional (default: 0)

    Returns
    -------
    str

    Examples
    --------
    >>> glyph_457(["","beta","gamma"], primary=0)
    'beta'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    n = len(routes)
    if n == 0:
        return ""
    for k in range(n):
        s = routes[(primary + k) % n]
        if str(s):
            return str(s)
    return ""
