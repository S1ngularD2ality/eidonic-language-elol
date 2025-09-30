# glyph_600.py — Zero Trust Validate
# -----------------------------------------------------------------------------
# ID:            600
# Pack:          Pack 006 (501–600)
# Name:          Zero Trust Validate
# Class:         policy_gate
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # pure predicate on claims
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any

def glyph_600(claims: Mapping[str, Any], *, require: Mapping[str, Any]) -> bool:
    """
    Zero Trust Validate — verify claim set satisfies all required predicates.

    Overview
    --------
    Performs simple equality and membership checks defined in `require`:
    - For scalar values: claims[k] == require[k]
    - For list/set values: require[k] ⊆ set(claims[k])

    Parameters
    ----------
    claims  : Mapping[str,Any]
    require : Mapping[str,Any]

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_600({'roles':['read','write'],'geo':'CA'}, require={'geo':'CA','roles':{'read'}})
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n + m)
    - Space : O(1)
    """
    for k, v in require.items():
        if isinstance(v, (list, set, tuple)):
            if set(v) - set(claims.get(k, [])):
                return False
        else:
            if claims.get(k) != v:
                return False
    return True
