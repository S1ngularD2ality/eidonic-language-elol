# glyph_685.py — HEALING_VISUAL_SCENE
# -----------------------------------------------------------------------------
# ID:            685
# Pack:          Pack 007 (601–700)
# Name:          HEALING_VISUAL_SCENE
# Class:         therapy.visual
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, List

def glyph_685(scenes: List[Dict], duration_s: int) -> Dict:
    """
    HEALING_VISUAL_SCENE — assemble a sequence of visual scenes with gentle transitions.

    Overview
    --------
    Each scene may include background color, vignette strength, and optional text cues.
    Transitions are crossfades with minimum 0.5 s.

    Parameters
    ----------
    scenes : List[Dict]
        e.g., {"rgb": [r,g,b], "hold_s": 8, "text": "soften jaw", "vignette": 0.2}
    duration_s : int
        Total cap; sequence repeats or truncates to fit.

    Returns
    -------
    Dict
        Visual scene plan with transitions.

    Examples
    --------
    >>> plan = glyph_685([{"rgb":[180,220,255],"hold_s":10}], 60)
    >>> plan["scenes"][0]["rgb"]
    [180, 220, 255]

    Exceptions
    ----------
    - ValueError : invalid colors or holds.

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n)
    """
    if duration_s < 10:
        raise ValueError("duration_s must be >= 10")
    norm = []
    for sc in scenes:
        r,g,b = sc.get("rgb",[0,0,0])
        hold  = float(sc.get("hold_s", 5.0))
        if any(not (0 <= c <= 255) for c in (r,g,b)):
            raise ValueError("rgb out of range")
        if hold <= 0:
            raise ValueError("hold_s must be > 0")
        norm.append({"rgb":[int(r),int(g),int(b)],"hold_s":hold,"text":sc.get("text"),"vignette":float(sc.get("vignette",0.0))})

    t, seq = 0.0, []
    i = 0
    while t < duration_s and norm:
        sc = norm[i % len(norm)]
        t += sc["hold_s"]
        seq.append(sc)
        i += 1

    return {"type":"visual_scene","duration_s":duration_s,"scenes":seq,"transition":{"type":"crossfade","min_s":0.5}}
