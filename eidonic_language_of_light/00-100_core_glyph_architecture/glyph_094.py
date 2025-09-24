# glyph_094.py — Liminal Flow Ascender
# -----------------------------------------------------------------------------
# ID:            094
# Pack:          Pack 001 (000–100)
# Name:          Liminal Flow Ascender
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

def glyph_094(seq: Sequence[float], *, threshold: float = 0.0, gain: float = 1.0) -> List[float]:
    """
    Liminal Flow Ascender — rectify above threshold then scale.

    Overview
    --------
    Returns `gain * max(x - threshold, 0)` for each element.

    Parameters
    ----------
    seq : Sequence[float]
    threshold : float, optional (default: 0.0)
    gain : float, optional (default: 1.0)

    Returns
    -------
    List[float]
        Ascended values.
    """
    th = float(threshold)
    g = float(gain)
    return [g * max(float(v) - th, 0.0) for v in seq]
