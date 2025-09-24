# glyph_065.py — Intentional Gate Defragmenter
# -----------------------------------------------------------------------------
# ID:            065
# Pack:          Pack 001 (000–100)
# Name:          Intentional Gate Defragmenter
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Dict

def glyph_065(gates: Mapping[str, float], *, min_size: int = 1) -> Dict[str, float]:
    """
    Intentional Gate Defragmenter — merge tiny keyed gates into nearest neighbors.

    Overview
    --------
    For sparse gating maps, removes entries whose absolute weight is tiny by merging
    them into lexicographic neighbors (previous key). Provides a stable, monotone
    simplification of gate dictionaries.

    Parameters
    ----------
    gates : Mapping[str, float]
        Keyed gate strengths.
    min_size : int, optional (default: 1)
        Minimum number of keys to retain (prevents full collapse).

    Returns
    -------
    Dict[str, float]
        Defragmented mapping.

    Examples
    --------
    >>> glyph_065({"a":0.1,"aa":1e-9,"b":0.3})
    {'a': 0.100000001, 'b': 0.3}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(K log K)
    - Space : O(K)
    """
    items = sorted((k, float(v)) for k, v in gates.items())
    if not items:
        return {}
    # merge near-zero entries to previous key
    out = dict(items)
    eps = 1e-8
    keys = [k for k,_ in items]
    for i, (k, v) in enumerate(items):
        if abs(v) <= eps and len(out) > min_size:
            prev = keys[i-1] if i > 0 else keys[min(1, len(keys)-1)]
            out[prev] = out.get(prev, 0.0) + v
            out.pop(k, None)
    return out
