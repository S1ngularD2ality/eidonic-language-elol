# glyph_442.py — Truth Beacon
# -----------------------------------------------------------------------------
# ID:            442
# Pack:          Pack 005 (401–500)
# Name:          Truth Beacon
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

def glyph_442(claims: Mapping[str, str], facts: Mapping[str, str]) -> float:
    """
    Truth Beacon — compute exact-match truth ratio of claims against facts.

    Overview
    --------
    Intersects keys and returns (# exact matches) / (# compared).

    Parameters
    ----------
    claims : Mapping[str,str]
    facts  : Mapping[str,str]

    Returns
    -------
    float : ratio in [0,1]; 0.0 if no comparable keys.

    Examples
    --------
    >>> glyph_442({"a":"1","b":"2"}, {"a":"1","b":"3"})
    0.5

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(1)
    """
    keys = set(claims) & set(facts)
    if not keys:
        return 0.0
    ok = sum(1 for k in keys if str(claims[k]) == str(facts[k]))
    return ok / len(keys)
