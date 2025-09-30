# glyph_687.py — GUIDED_MEDITATION_AUDIO
# -----------------------------------------------------------------------------
# ID:            687
# Pack:          Pack 007 (601–700)
# Name:          GUIDED_MEDITATION_AUDIO
# Class:         therapy.script
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, List

def glyph_687(script: List[Dict], duration_s: int) -> Dict:
    """
    GUIDED_MEDITATION_AUDIO — structure narration prompts over time.

    Overview
    --------
    Accepts timed segments with text and optional background tags. Produces a plan
    to render or perform narratively (externally).

    Parameters
    ----------
    script : List[Dict]
        e.g., {"t": 0, "text": "Relax the shoulders", "bg": "soft_ocean"}
    duration_s : int
        Session total time.

    Returns
    -------
    Dict
        Ordered narration plan.

    Examples
    --------
    >>> plan = glyph_687([{"t":0,"text":"arrive"},{"t":30,"text":"breathe"}], 120)
    >>> plan["segments"][1]["text"]
    'breathe'

    Exceptions
    ----------
    - ValueError : non-monotonic times or overrun.

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    if duration_s < 30:
        raise ValueError("duration_s must be >= 30")
    segs = sorted([{"t": float(s["t"]), "text": str(s["text"]), "bg": s.get("bg")} for s in script], key=lambda s: s["t"])
    if any(segs[i]["t"] < segs[i-1]["t"] for i in range(1, len(segs))):
        raise ValueError("script times must be non-decreasing")
    if segs and segs[-1]["t"] > duration_s:
        raise ValueError("last segment exceeds duration")
    return {"type":"guided_audio","duration_s":duration_s,"segments":segs}
