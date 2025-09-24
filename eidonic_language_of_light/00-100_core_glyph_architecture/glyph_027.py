# glyph_027.py — Subconscious Pulse Refiner
# -----------------------------------------------------------------------------
# ID:            027
# Pack:          Pack 001 (000–100)
# Name:          Subconscious Pulse Refiner
# Class:         filter
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_027(seq: Sequence[float], *, alpha: float = 0.2, beta: float = 0.1) -> List[float]:
    """
    Subconscious Pulse Refiner — two-stage smoothing (EMA followed by soft threshold).

    Overview
    --------
    First apply EMA with coefficient `alpha`, then shrink small magnitudes by
    y = sign(x) * max(|x|-beta, 0).

    Parameters
    ----------
    seq : Sequence[float]
    alpha : float, optional (default: 0.2)
    beta : float, optional (default: 0.1)

    Returns
    -------
    List[float]
        Refined sequence.

    Examples
    --------
    >>> glyph_027([0, 1, 0, 1], alpha=0.5, beta=0.1)
    [0.0, 0.45, 0.175, 0.5375]
    """
    if not seq:
        return []
    a = max(0.0, min(1.0, float(alpha)))
    b = max(0.0, float(beta))
    y = [float(seq[0])]
    for v in seq[1:]:
        y.append(a*float(v) + (1-a)*y[-1])
    out = []
    for v in y:
        s = -1.0 if v < 0 else (1.0 if v > 0 else 0.0)
        m = max(abs(v)-b, 0.0)
        out.append(s*m)
    return out
