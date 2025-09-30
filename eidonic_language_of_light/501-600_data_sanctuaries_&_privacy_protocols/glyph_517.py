# glyph_517.py — IP Block
# -----------------------------------------------------------------------------
# ID:            517
# Pack:          Pack 006 (501–600)
# Name:          IP Block
# Class:         auth_access_control
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # pure set logic
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Set

def glyph_517(ip: str, *, blocklist: Sequence[str]) -> bool:
    """
    IP Block — return True if `ip` is blocked.

    Overview
    --------
    Exact-match membership test, deterministic.

    Parameters
    ----------
    ip        : str
    blocklist : Sequence[str]

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_517('1.2.3.4', blocklist=['1.2.3.4'])
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1) average
    - Space : O(n)
    """
    return ip in set(blocklist)
