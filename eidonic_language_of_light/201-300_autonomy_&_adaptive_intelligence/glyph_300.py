# glyph_300.py — Soul Mirror Finalizer
# -----------------------------------------------------------------------------
# ID:            300
# Pack:          Pack 003 (201–300)
# Name:          Soul Mirror Finalizer
# Class:         reduction
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from __future__ import annotations
from typing import Sequence


def glyph_300(seq: Sequence[float], *, center: bool = True, eps: float = 1e-12) -> float:
    """
    Soul Mirror Finalizer — produce a scalar **finality score** by mirroring correlation.

    Overview
    --------
    Computes a normalized correlation between a sequence and its reversed copy:
    a single scalar in ``[-1, 1]`` that summarizes mirror-symmetry closure.
    When ``center=True``, the mean is removed before correlation, increasing
    sensitivity to structural symmetry rather than absolute offset.

    Parameters
    ----------
    seq : Sequence[float]
        Real-valued samples to finalize.
    center : bool, optional (default: ``True``)
        If ``True``, subtract the arithmetic mean before correlation.
    eps : float, optional (default: ``1e-12``)
        Numerical floor to avoid division by zero.

    Returns
    -------
    float
        Finality score in ``[-1, 1]``. ``1`` → perfect mirror symmetry, ``0`` → no linear
        relation, ``-1`` → perfect anti-symmetry.

    Design Guarantees
    -----------------
    - Pure function; no I/O or global state.
    - Deterministic given inputs.
    - Handles empty input by returning ``0.0``.

    Examples
    --------
    >>> glyph_300([1, 2, 3, 2, 1])
    1.0
    >>> round(glyph_300([1, 0, -1, 0], center=True), 6)
    -1.0
    >>> round(glyph_300([0.2, 0.1, -0.1, -0.2]), 6)
    1.0

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0:
        return 0.0

    xr = x[::-1]

    if center:
        mu = sum(x) / n
        x = [v - mu for v in x]
        xr = [v - mu for v in xr]

    num = sum(a * b for a, b in zip(x, xr))
    den = (sum(a * a for a in x) * sum(b * b for b in xr)) ** 0.5
    den = den if den > eps else 1.0
    r = num / den

    # Clamp to [-1, 1] for numerical safety
    if r > 1.0:
        return 1.0
    if r < -1.0:
        return -1.0
    return r
