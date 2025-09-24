# glyph_080.py — Frequency Lock Breaker
# -----------------------------------------------------------------------------
# ID:            080
# Pack:          Pack 001 (000–100)
# Name:          Frequency Lock Breaker
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_080(seq: Sequence[float], *, jitter: float = 0.01) -> List[float]:
    """
    Frequency Lock Breaker — inject micro-jitter to prevent phase locking.

    Overview
    --------
    Adds a small, deterministic pseudo-random perturbation that breaks exact
    periodic alignment without destroying structure.

    Parameters
    ----------
    seq : Sequence[float]
        Input samples.
    jitter : float, optional (default: 0.01)
        Amplitude of perturbation.

    Returns
    -------
    List[float]
        De-locked sequence.

    Examples
    --------
    >>> glyph_080([0,0,0,0], jitter=0.1)  # doctest: +ELLIPSIS
    [...]

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    out: List[float] = []
    # simple hash-based deterministic noise
    for i, v in enumerate(seq):
        h = (1103515245 * (i+12345) + 12345) & 0x7fffffff
        r = (h / 0x7fffffff) * 2.0 - 1.0
        out.append(float(v) + float(jitter)*r)
    return out
