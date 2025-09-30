# glyph_698.py — ENERGY_FIELD_HARMONY
# -----------------------------------------------------------------------------
# ID:            698
# Pack:          Pack 007 (601–700)
# Name:          ENERGY_FIELD_HARMONY
# Class:         guidance.harmonics
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, List

def glyph_698(weights: List[float]) -> Dict:
    """
    ENERGY_FIELD_HARMONY — normalize layer weights and emit harmony ratios.

    Overview
    --------
    Scales weights to sum to 1 and computes simple rational approximations between
    adjacent layers to guide harmonic blending.

    Parameters
    ----------
    weights : List[float]
        Non-negative values.

    Returns
    -------
    Dict
        {"weights":[...], "ratios":[(n,d), ...]}
    """
    if not weights or any(w < 0 for w in weights):
        raise ValueError("weights must be non-negative and non-empty")
    s = sum(weights)
    if s == 0:
        raise ValueError("sum of weights must be > 0")
    w = [wi / s for wi in weights]

    def approx_ratio(x: float, max_d: int = 16) -> tuple[int,int]:
        best = (1,1); err = abs(x - 1.0)
        for d in range(1, max_d+1):
            n = round(x * d)
            e = abs(x - (n/d))
            if e < err:
                best, err = (int(n), int(d)), e
        return best
    ratios = [approx_ratio(w[i+1]/w[i]) for i in range(len(w)-1)] if len(w) > 1 else []
    return {"type":"harmony","weights":w,"ratios":ratios}
