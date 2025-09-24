# glyph_203.py — Polarity Harmonic Bender
# -----------------------------------------------------------------------------
# ID:            203
# Pack:          Pack 003 (201–300)
# Name:          Polarity Harmonic Bender
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import math
from typing import Sequence, List

def glyph_203(seq: Sequence[float], *, gamma: float = 0.7) -> List[float]:
    """
    Polarity Harmonic Bender — compress magnitudes with signed power law.

    Overview
    --------
    y = sign(x) * |x|^gamma, with 0 < gamma <= 1.

    Parameters
    ----------
    seq : Sequence[float]
    gamma : float, optional (default: 0.7)

    Returns
    -------
    List[float]
        Bent sequence.

    Exceptions
    ----------
    - ValueError : if gamma <= 0.

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if gamma <= 0:
        raise ValueError("gamma must be > 0")
    g = float(gamma)
    out=[]
    for v in seq:
        if v == 0: out.append(0.0)
        else: out.append((1.0 if v>0 else -1.0) * (abs(float(v)) ** g))
    return out
