# glyph_091.py — Soul Pulse Navigator
# -----------------------------------------------------------------------------
# ID:            091
# Pack:          Pack 001 (000–100)
# Name:          Soul Pulse Navigator
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

def glyph_091(seq: Sequence[float], *, step: int, offset: int = 0) -> float:
    """
    Soul Pulse Navigator — stride-sample and return mean of visited points.

    Overview
    --------
    Walk indices `offset, offset+step, ...` within range, average the values.

    Parameters
    ----------
    seq : Sequence[float]
    step : int
    offset : int, optional (default: 0)

    Returns
    -------
    float
        Average along the navigation path (0.0 if no samples).
    """
    s = max(1, int(step))
    n = len(seq)
    xs = [float(seq[i]) for i in range(offset, n, s)]
    return (sum(xs) / len(xs)) if xs else 0.0
