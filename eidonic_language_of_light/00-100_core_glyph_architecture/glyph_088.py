# glyph_088.py — Harmonic Feedback Deflector
# -----------------------------------------------------------------------------
# ID:            088
# Pack:          Pack 001 (000–100)
# Name:          Harmonic Feedback Deflector
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_088(seq: Sequence[float], *, max_gain: float = 1.2) -> bool:
    """
    Harmonic Feedback Deflector — guard against runaway accumulation.

    Overview
    --------
    Returns True if any cumulative sum prefix exceeds `max_gain` times the
    absolute mean magnitude; else False. A safety gate for feedback loops.

    Parameters
    ----------
    seq : Sequence[float]
    max_gain : float, optional (default: 1.2)

    Returns
    -------
    bool
        Whether feedback looks unstable.

    Examples
    --------
    >>> glyph_088([1,1,10,1], max_gain=2.0)
    True
    """
    x = [abs(float(v)) for v in seq]
    if not x:
        return False
    mean = (sum(x) / len(x)) or 1.0
    s = 0.0
    for v in x:
        s += v
        if s > max_gain * mean * len(x):
            return True
    return False
