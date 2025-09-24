# glyph_100.py — Dimensional Flame Finalizer
# -----------------------------------------------------------------------------
# ID:            100
# Pack:          Pack 001 (000–100)
# Name:          Dimensional Flame Finalizer
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_100(settings: Mapping[str, Any], *, strict: bool = True) -> Dict[str, Any]:
    """
    Dimensional Flame Finalizer — enforce final packing rules on settings.

    Overview
    --------
    Applies canonicalization:
    - remove `None` values,
    - sort tuple/list values,
    - if `strict`, raise on empty strings and NaNs.

    Parameters
    ----------
    settings : Mapping[str, Any]
    strict : bool, optional (default: True)

    Returns
    -------
    Dict[str, Any]
        Finalized settings.

    Examples
    --------
    >>> glyph_100({"a": None, "b": [2,1], "c": ""}, strict=False)
    {'b': [1, 2], 'c': ''}

    Exceptions
    ----------
    - ValueError : if strict and invalid values encountered.

    Complexity
    ----------
    - Time  : O(K log L) across list/tuple lengths
    - Space : O(K + total L)
    """
    import math
    out: Dict[str, Any] = {}
    for k, v in settings.items():
        if v is None:
            continue
        if isinstance(v, (list, tuple)):
            vv = sorted(v)
        else:
            vv = v
        if strict:
            if isinstance(vv, str) and vv == "":
                raise ValueError(f"empty string for key '{k}'")
            if isinstance(vv, (float,)) and math.isnan(vv):
                raise ValueError(f"NaN for key '{k}'")
        out[k] = vv
    return out
