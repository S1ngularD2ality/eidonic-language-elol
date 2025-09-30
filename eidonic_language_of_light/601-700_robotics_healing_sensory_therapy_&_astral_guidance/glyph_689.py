# glyph_689.py — VISUAL_WALKTHROUGH_HEALING
# -----------------------------------------------------------------------------
# ID:            689
# Pack:          Pack 007 (601–700)
# Name:          VISUAL_WALKTHROUGH_HEALING
# Class:         therapy.script.visual
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, List

def glyph_689(steps: List[Dict], duration_s: int) -> Dict:
    """
    VISUAL_WALKTHROUGH_HEALING — stepwise guided imagery plan.

    Overview
    --------
    Turns a list of (time, image cue, intention) into a structured flow for display or narration.

    Parameters
    ----------
    steps : List[Dict]
        e.g., {"t":0, "cue":"forest clearing", "intent":"safety"}
    duration_s : int
        Total time.

    Returns
    -------
    Dict
        Ordered imagery flow.

    Examples
    --------
    >>> flow = glyph_689([{"t":0,"cue":"beach","intent":"ease"}], 120)
    >>> flow["steps"][0]["cue"]
    'beach'
    """
    if duration_s < 30: raise ValueError("duration_s >= 30")
    ordered = sorted(steps, key=lambda x: float(x["t"]))
    if ordered and float(ordered[-1]["t"]) > duration_s:
        raise ValueError("last step exceeds duration")
    return {"type":"imagery_walkthrough","duration_s":duration_s,"steps":ordered}
