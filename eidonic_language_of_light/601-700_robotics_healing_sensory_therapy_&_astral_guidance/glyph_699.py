# glyph_699.py — SACRED_TONE_RES
# -----------------------------------------------------------------------------
# ID:            699
# Pack:          Pack 007 (601–700)
# Name:          SACRED_TONE_RES
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

def glyph_699(freqs: List[float]) -> Dict:
    """
    SACRED_TONE_RES — evaluate consonance via small-integer interval matches.

    Overview
    --------
    For consecutive frequencies, computes nearest simple ratios (e.g., 3:2, 4:3, 5:4)
    and scores consonance (lower error → higher score).

    Parameters
    ----------
    freqs : List[float]
        Positive frequencies in Hz.

    Returns
    -------
    Dict
        {"pairs":[{"a":f1,"b":f2,"ratio":"3:2","error":0.01}, ...], "score":0..1}
    """
    if len(freqs) < 2 or any(f <= 0 for f in freqs):
        raise ValueError("need >=2 positive frequencies")
    candidates = [(2,1),(3,2),(4,3),(5,4),(6,5)]
    pairs = []
    total_err = 0.0
    for a,b in zip(freqs, freqs[1:]):
        r = b/a
        best = min(candidates, key=lambda p: abs(r - (p[0]/p[1])))
        err = abs(r - (best[0]/best[1]))
        total_err += err
        pairs.append({"a":a,"b":b,"ratio":f"{best[0]}:{best[1]}","error":err})
    score = max(0.0, 1.0 - total_err / len(pairs))
    return {"type":"tone_resonance","pairs":pairs,"score":score}
