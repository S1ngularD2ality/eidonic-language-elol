# glyph_482.py — Sanity Check
# -----------------------------------------------------------------------------
# ID:            482
# Pack:          Pack 005 (401–500)
# Name:          Sanity Check
# Class:         verifier
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Sequence

def glyph_482(values: Mapping[str, float], required: Sequence[str]) -> bool:
    """
    Sanity Check — True when all required keys exist and are finite numbers.

    Overview
    --------
    Validates presence and that float(..) neither inf nor NaN.

    Parameters
    ----------
    values   : Mapping[str,float]
    required : Sequence[str]

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_482({'a':1.0,'b':0.0}, ['a','b'])
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    import math
    for k in required:
        if k not in values:
            return False
        x = float(values[k])
        if math.isnan(x) or math.isinf(x):
            return False
    return True
