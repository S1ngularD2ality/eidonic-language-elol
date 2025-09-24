# glyph_024.py — Polarity Pulse Amplifier
# -----------------------------------------------------------------------------
# ID:            024
# Pack:          Pack 001 (000–100)
# Name:          Polarity Pulse Amplifier
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

def glyph_024(seq: Sequence[float], *, pos_gain: float = 1.5, neg_gain: float = 1.0) -> List[float]:
    """
    Polarity Pulse Amplifier — apply different gains to positive vs negative values.

    Overview
    --------
    For x>=0 multiply by pos_gain; for x<0 multiply by neg_gain. Keeps zeros unchanged.

    Parameters
    ----------
    seq : Sequence[float]
        Input samples.
    pos_gain : float, optional (default: 1.5)
    neg_gain : float, optional (default: 1.0)

    Returns
    -------
    List[float]
        Gain-adjusted sequence.

    Examples
    --------
    >>> glyph_024([-1, 0, 2], pos_gain=2.0, neg_gain=0.5)
    [-0.5, 0.0, 4.0]
    """
    pg, ng = float(pos_gain), float(neg_gain)
    return [x*pg if (x:=float(v))>=0 else x*ng for v in seq]
