# glyph_444.py — Context Binder
# -----------------------------------------------------------------------------
# ID:            444
# Pack:          Pack 005 (401–500)
# Name:          Context Binder
# Class:         binder
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_444(context: Mapping[str, Any], patch: Mapping[str, Any]) -> Dict[str, Any]:
    """
    Context Binder — immutably merge a patch into context with shallow precedence.

    Overview
    --------
    Returns a new dict where `patch` keys overwrite existing ones.

    Parameters
    ----------
    context : Mapping[str,Any]
    patch   : Mapping[str,Any]

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_444({"a":1},{"a":2,"b":3})
    {'a': 2, 'b': 3}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    out = dict(context)
    out.update({k: v for k, v in patch.items()})
    return out
