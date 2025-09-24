# glyph_098.py — Harmonic Sequence Encoder
# -----------------------------------------------------------------------------
# ID:            098
# Pack:          Pack 001 (000–100)
# Name:          Harmonic Sequence Encoder
# Class:         generator
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import List

def glyph_098(n: int, *, base: float = 1.0, ratio: float = 2.0) -> List[float]:
    """
    Harmonic Sequence Encoder — geometric progression of length n.

    Overview
    --------
    Emits `[base * ratio^i for i in 0..n-1]`.

    Parameters
    ----------
    n : int
    base : float, optional (default: 1.0)
    ratio : float, optional (default: 2.0)

    Returns
    -------
    List[float]
        Harmonic ladder.
    """
    if n < 0:
        return []
    return [float(base) * (float(ratio) ** i) for i in range(n)]
