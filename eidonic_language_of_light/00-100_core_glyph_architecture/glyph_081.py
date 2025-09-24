# glyph_081.py — Polarity Gate Reducer
# -----------------------------------------------------------------------------
# ID:            081
# Pack:          Pack 001 (000–100)
# Name:          Polarity Gate Reducer
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Dict

def glyph_081(gates: Mapping[str, float], *, floor: float = 1e-8) -> Dict[str, float]:
    """
    Polarity Gate Reducer — collapse nearly-canceling positive/negative pairs.

    Overview
    --------
    For keys that appear as `k` and `!k` (negation form), combine their magnitudes:
    `g[k] := g[k] - g[!k]`. Entries whose absolute value ≤ floor are removed.
    Useful to simplify opposing gates before routing.

    Parameters
    ----------
    gates : Mapping[str, float]
        Mapping of gate names to strengths. Negations use a '!' prefix.
    floor : float, optional (default: 1e-8)
        Magnitudes below or equal to this are discarded.

    Returns
    -------
    Dict[str, float]
        Reduced gate mapping with negations eliminated.

    Examples
    --------
    >>> glyph_081({"a": 0.7, "!a": 0.6, "b": 0.1})
    {'a': 0.09999999999999998}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(K)
    - Space : O(K)
    """
    pos: Dict[str, float] = {}
    neg: Dict[str, float] = {}
    for k, v in gates.items():
        if k.startswith("!"):
            neg[k[1:]] = neg.get(k[1:], 0.0) + float(v)
        else:
            pos[k] = pos.get(k, 0.0) + float(v)
    out: Dict[str, float] = {}
    keys = set(pos) | set(neg)
    for k in keys:
        val = pos.get(k, 0.0) - neg.get(k, 0.0)
        if abs(val) > float(floor):
            out[k] = val
    return out
