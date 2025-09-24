# glyph_239.py — Harmonic Symmetry Fracturer
# -----------------------------------------------------------------------------
# ID:            239
# Pack:          Pack 003 (201–300)
# Name:          Harmonic Symmetry Fracturer
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_003.md', manifest_json='glyph_manifest_pack_003.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_239(seq: Sequence[float], *, asym: float = 0.25) -> List[float]:
    """
    Harmonic Symmetry Fracturer — mix with a shifted copy to break symmetry.

    Overview
    --------
    y[i] = (1-a)*x[i] + a*x[(i+1) mod n], with a ∈ [0,1].

    Parameters
    ----------
    seq : Sequence[float]
    asym : float, optional (default: 0.25)

    Returns
    -------
    List[float]
        Fractured sequence.
    """
    x = [float(v) for v in seq]
    n = len(x)
    if n == 0: return []
    a = max(0.0, min(1.0, float(asym)))
    return [(1-a)*x[i] + a*x[(i+1) % n] for i in range(n)]
