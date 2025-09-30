# glyph_693.py — ASTRAL_PATH_TRACK
# -----------------------------------------------------------------------------
# ID:            693
# Pack:          Pack 007 (601–700)
# Name:          ASTRAL_PATH_TRACK
# Class:         guidance.astral
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, List, Tuple

def glyph_693(checkpoints: List[Tuple[str, float]]) -> Dict:
    """
    ASTRAL_PATH_TRACK — record symbolic checkpoints and elapsed times.

    Overview
    --------
    Returns a breadcrumb trail for reflective practice; consumers may visualize externally.

    Parameters
    ----------
    checkpoints : List[Tuple[str, float]]
        Pairs of (label, t_seconds).

    Returns
    -------
    Dict
        Structured path with simple stats.
    """
    cps = [{"label": str(lbl), "t": float(t)} for lbl, t in checkpoints]
    cps = sorted(cps, key=lambda c: c["t"])
    spans = [cps[i]["t"] - cps[i-1]["t"] for i in range(1, len(cps))] if len(cps) > 1 else []
    return {"type":"astral_path","checkpoints":cps,"stats":{"segments":len(spans),"total_s":(cps[-1]["t"] if cps else 0.0)}}
