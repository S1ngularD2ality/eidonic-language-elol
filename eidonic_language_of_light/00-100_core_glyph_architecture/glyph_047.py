# glyph_047.py — Inner Sequence Stabilizer
# -----------------------------------------------------------------------------
# ID:            047
# Pack:          Pack 001 (000–100)
# Name:          Inner Sequence Stabilizer
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_047(seq: Sequence[float], *, alpha: float = 0.2) -> List[float]:
    """
    Inner Sequence Stabilizer — exponential moving average (EMA) smoothing.

    Overview
    --------
    Produces `y[0]=x[0]`; `y[t]=alpha*x[t]+(1-alpha)*y[t-1]`. Reflection-free,
    single-pass stabilizer for noisy streams.

    Parameters
    ----------
    seq : Sequence[float]
        Input sequence.
    alpha : float, optional (default: 0.2)
        Smoothing factor in [0,1]. Smaller → smoother.

    Returns
    -------
    List[float]
        Smoothed sequence.

    Examples
    --------
    >>> glyph_047([0, 1, 0, 1], alpha=0.5)
    [0.0, 0.5, 0.25, 0.625]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if not seq:
        return []
    a = min(1.0, max(0.0, float(alpha)))
    out: List[float] = [float(seq[0])]
    for v in seq[1:]:
        out.append(a * float(v) + (1 - a) * out[-1])
    return out
