# glyph_111.py — Harmonic Gate Ascender
# -----------------------------------------------------------------------------
# ID:            111
# Pack:          Pack 002 (101–200)
# Name:          Harmonic Gate Ascender
# Class:         filter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_111(seq: Sequence[float], *, slope: float = 1.0, bias: float = 0.0) -> List[float]:
    """
    Harmonic Gate Ascender — smooth rectifier (softplus with bias).

    Overview
    --------
    y = log(1 + exp(slope*(x - bias))) + bias.

    Parameters
    ----------
    seq : Sequence[float]
    slope : float, optional (default: 1.0)
    bias : float, optional (default: 0.0)

    Returns
    -------
    List[float]
        Ascended values.

    Examples
    --------
    >>> glyph_111([-1,0,1], slope=2.0, bias=0.0)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    s = max(1e-6, float(slope))
    b = float(bias)
    return [math.log1p(math.exp(s*(float(v)-b))) + b for v in seq]
