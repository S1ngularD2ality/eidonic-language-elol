# glyph_407.py — Load Balancer
# -----------------------------------------------------------------------------
# ID:            407
# Pack:          Pack 005 (401–500)
# Name:          Load Balancer
# Class:         allocator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Dict

def glyph_407(loads: Mapping[str, float], incoming: float) -> Dict[str, float]:
    """
    Load Balancer — distribute incoming work inversely to current load.

    Overview
    --------
    Computes weights 1/max(load,ε), normalizes, and multiplies by `incoming`.

    Parameters
    ----------
    loads    : Mapping[str,float] — current per-agent load
    incoming : float              — total work units to distribute

    Returns
    -------
    Dict[str, float] : allocation per agent

    Examples
    --------
    >>> glyph_407({"a":2.0,"b":1.0}, 3.0)
    {'a': 1.0, 'b': 2.0}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    inv = {k: 1.0 / max(1e-12, float(v)) for k, v in loads.items()}
    s = sum(inv.values()) or 1.0
    return {k: incoming * (w / s) for k, w in inv.items()}
