# glyph_136.py — Subdimensional Core Amplifier
# -----------------------------------------------------------------------------
# ID:            136
# Pack:          Pack 002 (101–200)
# Name:          Subdimensional Core Amplifier
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

def glyph_136(seq: Sequence[float], *, boost: float = 1.5, center: float = 0.0) -> List[float]:
    """
    Subdimensional Core Amplifier — saturating boost around a center.

    Overview
    --------
    y = center + tanh(boost*(x-center)).

    Parameters
    ----------
    seq : Sequence[float]
    boost : float, optional (default: 1.5)
    center : float, optional (default: 0.0)

    Returns
    -------
    List[float]
        Amplified series.
    """
    import math
    b = float(boost); c = float(center)
    return [c + math.tanh(b*(float(v)-c)) for v in seq]
