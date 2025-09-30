# glyph_509.py — Token Gate
# -----------------------------------------------------------------------------
# ID:            509
# Pack:          Pack 006 (501–600)
# Name:          Token Gate
# Class:         auth_access_control
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Set

def glyph_509(token: Mapping[str, Any], *, allowed: Set[str], now: int) -> bool:
    """
    Token Gate — whitelist + expiry check.

    Overview
    --------
    Allows if token['sub'] ∈ allowed and `now <= token['exp']` (integer seconds).

    Parameters
    ----------
    token   : Mapping[str,Any]  (expects 'sub':str, 'exp':int)
    allowed : Set[str]
    now     : int

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_509({'sub':'a','exp':10}, allowed={'a'}, now=9)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    sub = str(token.get("sub", ""))
    exp = int(token.get("exp", -1))
    return (sub in allowed) and (now <= exp)
