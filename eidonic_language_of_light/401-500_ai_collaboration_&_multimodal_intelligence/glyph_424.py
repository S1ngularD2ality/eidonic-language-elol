# glyph_424.py — Semantic Fuse
# -----------------------------------------------------------------------------
# ID:            424
# Pack:          Pack 005 (401–500)
# Name:          Semantic Fuse
# Class:         fusion
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Dict, Set

def glyph_424(scores_a: Mapping[str, float], scores_b: Mapping[str, float], *, w_a: float = 0.5) -> Dict[str, float]:
    """
    Semantic Fuse — convex blend of two label→score maps.

    Overview
    --------
    Union all labels; output ``max(0, w_a*A + (1-w_a)*B)`` per label.

    Parameters
    ----------
    scores_a : Mapping[str, float]
    scores_b : Mapping[str, float]
    w_a : float, optional
        Blend weight for A in [0,1] (default: 0.5).

    Returns
    -------
    Dict[str, float]

    Examples
    --------
    >>> glyph_424({"cat":0.6}, {"cat":0.4,"dog":0.9}, w_a=0.5)
    {'cat': 0.5, 'dog': 0.45}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(k)
    """
    w = max(0.0, min(1.0, float(w_a)))
    keys: Set[str] = set(scores_a) | set(scores_b)
    return {k: max(0.0, w*float(scores_a.get(k,0.0)) + (1.0-w)*float(scores_b.get(k,0.0))) for k in keys}
