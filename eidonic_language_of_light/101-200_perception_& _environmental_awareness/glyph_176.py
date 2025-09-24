# glyph_176.py — Polarity Lens Divider
# -----------------------------------------------------------------------------
# ID:            176
# Pack:          Pack 002 (101–200)
# Name:          Polarity Lens Divider
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

def glyph_176(seq: Sequence[float]) -> Tuple[List[float], List[float]]:
    """
    Polarity Lens Divider — separate negative and non-negative values.

    Overview
    --------
    Returns (negatives, non_negatives) preserving order.

    Parameters
    ----------
    seq : Sequence[float]

    Returns
    -------
    (List[float], List[float])
        (neg, nonneg)
    """
    neg = [float(v) for v in seq if float(v) < 0]
    non = [float(v) for v in seq if float(v) >= 0]
    return neg, non
