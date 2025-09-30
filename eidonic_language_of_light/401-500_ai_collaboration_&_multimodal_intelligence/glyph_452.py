# glyph_452.py — Context Mirror
# -----------------------------------------------------------------------------
# ID:            452
# Pack:          Pack 005 (401–500)
# Name:          Context Mirror
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_452(payload: Mapping[str, Any], *, center: str = "data") -> Dict[str, Any]:
    """
    Context Mirror — reflect key names around a center tag.

    Overview
    --------
    For keys 'left'/'right' variants, swap them; otherwise pass through.

    Parameters
    ----------
    payload : Mapping[str,Any]
    center  : str, optional (default: "data")

    Returns
    -------
    Dict[str,Any]

    Examples
    --------
    >>> glyph_452({"left":1,"right":2,"data":3})
    {'left': 2, 'right': 1, 'data': 3}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(k)
    """
    out = dict(payload)
    L, R = "left", "right"
    if L in out or R in out:
        out[L], out[R] = out.get(R, out.get(L)), out.get(L, out.get(R))
    out[center] = out.get(center, out.get("data", None))
    return out
