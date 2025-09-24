# glyph_186.py — Polarity Signal Scrambler
# -----------------------------------------------------------------------------
# ID:            186
# Pack:          Pack 002 (101–200)
# Name:          Polarity Signal Scrambler
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

def glyph_186(seq: Sequence[float], *, seed: int = 0) -> List[float]:
    """
    Polarity Signal Scrambler — deterministic sign scrambling.

    Overview
    --------
    Multiplies x[i] by sgn where sgn = sign(sin( (i+1)*(seed+1)*π/2 )) ∈ {-1, +1}.

    Parameters
    ----------
    seq : Sequence[float]
    seed : int, optional (default: 0)

    Returns
    -------
    List[float]
        Scrambled sequence.

    Examples
    --------
    >>> glyph_186([1,1,1,1], seed=1)
    [1.0, -1.0, 1.0, -1.0]
    """
    out: List[float] = []
    k = (int(seed) + 1)
    for i, v in enumerate(seq, start=1):
        sgn = 1.0 if math.sin(i * k * math.pi/2.0) >= 0 else -1.0
        out.append(float(v) * sgn)
    return out
