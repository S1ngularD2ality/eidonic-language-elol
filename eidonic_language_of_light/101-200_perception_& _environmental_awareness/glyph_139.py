# glyph_139.py — Spiral Flame Infuser
# -----------------------------------------------------------------------------
# ID:            139
# Pack:          Pack 002 (101–200)
# Name:          Spiral Flame Infuser
# Class:         transform
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-23
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_002.md', manifest_json='glyph_manifest_pack_002.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List

def glyph_139(seq: Sequence[float], *, ratio: float = 0.5) -> List[float]:
    """
    Spiral Flame Infuser — mix with the mirrored sequence using ratio.

    Overview
    --------
    y[i] = (1-r)*x[i] + r*x[n-1-i], r∈[0,1].

    Parameters
    ----------
    seq : Sequence[float]
    ratio : float, optional (default: 0.5)

    Returns
    -------
    List[float]
        Infused series.
    """
    r = max(0.0, min(1.0, float(ratio)))
    x = [float(v) for v in seq]
    n = len(x)
    return [(1-r)*x[i] + r*x[n-1-i] for i in range(n)]
