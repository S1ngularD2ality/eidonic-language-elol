# glyph_416.py — Guardian Handshake
# -----------------------------------------------------------------------------
# ID:            416
# Pack:          Pack 005 (401–500)
# Name:          Guardian Handshake
# Class:         verifier
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping

def glyph_416(claims: Mapping[str, str], rules: Mapping[str, str]) -> bool:
    """
    Guardian Handshake — exact-match verification of identity claims.

    Overview
    --------
    Returns True only if every (key,value) in rules matches exactly in claims.

    Parameters
    ----------
    claims : Mapping[str,str]
    rules  : Mapping[str,str]

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_416({"id":"x","tier":"gold"}, {"tier":"gold"})
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(1)
    """
    for k, v in rules.items():
        if str(claims.get(k, "")) != str(v):
            return False
    return True
