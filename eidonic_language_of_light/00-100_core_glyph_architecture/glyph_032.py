# glyph_032.py — Inner Voice Amplifier
# -----------------------------------------------------------------------------
# ID:            032
# Pack:          Pack 001 (000–100)
# Name:          Inner Voice Amplifier
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
import math

def glyph_032(seq: Sequence[float], *, gain: float = 2.0, bias: float = 0.0) -> List[float]:
    """
    Inner Voice Amplifier — smooth saturating boost around a bias center.

    Overview
    --------
    Applies y = tanh(gain*(x - bias)) + bias to emphasize articulation without clipping.

    Parameters
    ----------
    seq : Sequence[float]
    gain : float, optional (default: 2.0)
    bias : float, optional (default: 0.0)

    Returns
    -------
    List[float]
        Amplified sequence.
    """
    g, b = float(gain), float(bias)
    return [math.tanh(g*(float(v)-b)) + b for v in seq]
