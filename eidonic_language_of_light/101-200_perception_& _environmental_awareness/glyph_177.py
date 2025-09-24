# glyph_177.py — Thought Gate Inhibitor
# -----------------------------------------------------------------------------
# ID:            177
# Pack:          Pack 002 (101–200)
# Name:          Thought Gate Inhibitor
# Class:         control
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_177(seq: Sequence[float], *, threshold: float) -> List[float]:
    """
    Thought Gate Inhibitor — hard gate values below a threshold.

    Overview
    --------
    y[i] = x[i] if x[i] >= threshold else 0.

    Parameters
    ----------
    seq : Sequence[float]
    threshold : float

    Returns
    -------
    List[float]
        Inhibited sequence.
    """
    th = float(threshold)
    return [float(v) if float(v) >= th else 0.0 for v in seq]
