# glyph_022.py — Anchor Gate Refractor
# -----------------------------------------------------------------------------
# ID:            022
# Pack:          Pack 001 (000–100)
# Name:          Anchor Gate Refractor
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Dict

def glyph_022(weights: Mapping[str, float], *, gamma: float = 0.5) -> Dict[str, float]:
    """
    Anchor Gate Refractor — compress extreme gate weights with signed gamma curve.

    Overview
    --------
    Applies y = sign(x) * |x|^gamma with 0<gamma<=1 to reduce disparity while preserving
    ordering and sign. Useful for “refracting” anchors into a gentler spread.

    Parameters
    ----------
    weights : Mapping[str, float]
        Gate/anchor weights (any real values).
    gamma : float, optional (default: 0.5)
        Compression exponent, 0 < gamma <= 1.

    Returns
    -------
    Dict[str, float]
        Refracted weights.

    Examples
    --------
    >>> glyph_022({"a": 1.0, "b": 100.0}, gamma=0.5)
    {'a': 1.0, 'b': 10.0}

    Exceptions
    ----------
    - ValueError : if gamma <= 0.

    Complexity
    ----------
    - Time  : O(K)
    - Space : O(K)
    """
    if gamma <= 0:
        raise ValueError("gamma must be > 0")
    g = float(gamma)
    out: Dict[str, float] = {}
    for k, v in weights.items():
        s = -1.0 if v < 0 else (1.0 if v > 0 else 0.0)
        out[k] = s * (abs(float(v)) ** g)
    return out
