# glyph_142.py — Recursive Gate Equalizer
# -----------------------------------------------------------------------------
# ID:            142
# Pack:          Pack 002 (101–200)
# Name:          Recursive Gate Equalizer
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Dict

def glyph_142(gates: Mapping[str, float], *, depth: int = 2) -> Dict[str, float]:
    """
    Recursive Gate Equalizer — iteratively compress disparities.

    Overview
    --------
    Repeats: normalize by max |v|, then apply signed sqrt. `depth` controls repeats.

    Parameters
    ----------
    gates : Mapping[str, float]
    depth : int, optional (default: 2)

    Returns
    -------
    Dict[str, float]
        Equalized gate strengths.

    Examples
    --------
    >>> glyph_142({"a": 9.0, "b": 1.0}, depth=1)
    {'a': 1.0, 'b': 0.3333333333333333}
    """
    out = {k: float(v) for k, v in gates.items()}
    for _ in range(max(0, depth)):
        if not out: break
        mx = max(abs(v) for v in out.values()) or 1.0
        out = {k: (1.0 if v>0 else (-1.0 if v<0 else 0.0)) * (abs(v/mx) ** 0.5) for k, v in out.items()}
    return out
