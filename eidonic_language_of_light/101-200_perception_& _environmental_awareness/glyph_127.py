# glyph_127.py — Intention Channel Splitter
# -----------------------------------------------------------------------------
# ID:            127
# Pack:          Pack 002 (101–200)
# Name:          Intention Channel Splitter
# Class:         analyzer
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Tuple, List

def glyph_127(seq: Sequence[float], *, threshold: float = 0.0) -> Tuple[List[float], List[float]]:
    """
    Intention Channel Splitter — bifurcate by sign around a threshold.

    Overview
    --------
    Returns (low_channel, high_channel) where low = {x ≤ threshold}, high = {x > threshold}.

    Parameters
    ----------
    seq : Sequence[float]
    threshold : float, optional (default: 0.0)

    Returns
    -------
    (List[float], List[float])
        (low, high)
    """
    low = [float(v) for v in seq if float(v) <= threshold]
    high = [float(v) for v in seq if float(v) > threshold]
    return low, high
