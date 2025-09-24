# glyph_194.py — Thought Drift Realigner
# -----------------------------------------------------------------------------
# ID:            194
# Pack:          Pack 002 (101–200)
# Name:          Thought Drift Realigner
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List, Tuple

def glyph_194(seq: Sequence[float]) -> Tuple[List[float], float, float]:
    """
    Thought Drift Realigner — detrend by least squares line fit.

    Overview
    --------
    Fits y = a*t + b; returns residuals r[t] = x[t] - (a*t + b) and (a, b).

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], float, float)
        (residuals, slope, intercept)

    Examples
    --------
    >>> r, a, b = glyph_194([0,1,2,3,4])
    >>> round(a, 6)
    1.0
    """
    n = len(seq)
    if n == 0:
        return [], 0.0, 0.0
    xs = list(range(n))
    sx = sum(xs); sy = sum(float(v) for v in seq)
    sxx = sum(x*x for x in xs); sxy = sum(x*float(v) for x,v in zip(xs, seq))
    denom = n*sxx - sx*sx or 1.0
    a = (n*sxy - sx*sy) / denom
    b = (sy - a*sx) / n
    residuals = [float(v) - (a*t + b) for t, v in enumerate(seq)]
    return residuals, a, b
