# glyph_691.py — AROMA_CUE
# -----------------------------------------------------------------------------
# ID:            691
# Pack:          Pack 007 (601–700)
# Name:          AROMA_CUE
# Class:         therapy.olfactory
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, List

def glyph_691(schedule: List[Dict], profile: Dict | None = None) -> Dict:
    """
    AROMA_CUE — schedule timed scent diffusion with safety checks.

    Overview
    --------
    Emits diffusion pulses with intensity caps and **allergy/opt-out flags**. No hardware I/O.

    Parameters
    ----------
    schedule : List[Dict]
        Each: {"t": seconds, "blend": "lavender", "intensity": 0..1, "duration_s": >0}
    profile : Dict, optional
        Allergy information, e.g., {"avoid": ["citrus"]}

    Returns
    -------
    Dict
        Olfactory plan.

    Examples
    --------
    >>> plan = glyph_691([{"t":0,"blend":"lavender","intensity":0.3,"duration_s":10}], {"avoid":["citrus"]})
    >>> plan["safety"]["opt_out"]
    True
    """
    avoid = set((profile or {}).get("avoid", []))
    pulses = []
    for p in schedule:
        t = float(p["t"]); blend = str(p["blend"]); inten = float(p["intensity"]); d = float(p["duration_s"])
        if d <= 0 or not (0.0 <= inten <= 1.0):
            raise ValueError("invalid intensity/duration")
        pulses.append({"t":t,"blend":blend,"intensity":inten,"duration_s":d,"skip":blend in avoid})
    return {"type":"aroma_session","pulses":pulses,"safety":{"opt_out":True,"allergy_profile":list(avoid)}}
