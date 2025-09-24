# glyph_166.py — Frequency Pattern Reflector
# -----------------------------------------------------------------------------
# ID:            166
# Pack:          Pack 002 (101–200)
# Name:          Frequency Pattern Reflector
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_166(seq: Sequence[float], *, mix: float = 0.5) -> List[float]:
    """
    Frequency Pattern Reflector — enforce circular mirror symmetry in phase.

    Overview
    --------
    Mixes each sample with its circular reverse:
      y[i] = (1-mix)*x[i] + mix*x[(n-i) % n].
    This acts like a coarse "frequency reflection" without explicit FFT.

    Parameters
    ----------
    seq : Sequence[float]
    mix : float, optional (default: 0.5)

    Returns
    -------
    List[float]
        Reflected series.

    Examples
    --------
    >>> glyph_166([1,2,3,4], mix=1.0)
    [4.0, 3.0, 2.0, 1.0]
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0:
        return []
    m = max(0.0, min(1.0, float(mix)))
    return [(1-m)*x[i] + m*x[(n-i) % n] for i in range(n)]
