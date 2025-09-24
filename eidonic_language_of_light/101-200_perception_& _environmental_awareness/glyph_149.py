# glyph_149.py — Polarity Thought Mender
# -----------------------------------------------------------------------------
# ID:            149
# Pack:          Pack 002 (101–200)
# Name:          Polarity Thought Mender
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_149(seq: Sequence[float], *, bias: float = 0.0, gain: float = 1.0) -> List[float]:
    """
    Polarity Thought Mender — soften negatives, preserve positives.

    Overview
    --------
    Applies y = max(x, 0) + tanh(gain*min(x, 0)) + bias.

    Parameters
    ----------
    seq : Sequence[float]
    bias : float, optional (default: 0.0)
    gain : float, optional (default: 1.0)

    Returns
    -------
    List[float]
        Mended values.
    """
    import math
    g = float(gain); b = float(bias)
    out=[]
    for v in seq:
        x=float(v)
        out.append(max(x,0.0) + math.tanh(g*min(x,0.0)) + b)
    return out
