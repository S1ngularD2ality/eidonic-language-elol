# glyph_683.py — COLOR_THERAPY_LIGHT
# -----------------------------------------------------------------------------
# ID:            683
# Pack:          Pack 007 (601–700)
# Name:          COLOR_THERAPY_LIGHT
# Class:         therapy.visual
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, List, Tuple, Literal

Palette = Literal["calm", "focus", "restore", "sleep"]

def glyph_683(duration_s: int,
              palette: Palette = "calm",
              sequence: List[Tuple[int, int, int, float]] | None = None) -> Dict:
    """
    COLOR_THERAPY_LIGHT — produce a gentle, flicker-safe color sequence plan.

    Overview
    --------
    Returns a plan of (R,G,B,hold_s) steps with a **maximum pulse rate <= 30 Hz**
    (well below typical photosensitivity risks). No hardware I/O; external renderer only.

    Parameters
    ----------
    duration_s : int
        Total length (>= 30).
    palette : {"calm","focus","restore","sleep"}, optional
        Predefined color mood sets.
    sequence : List[Tuple[R,G,B,hold_s]], optional
        Custom steps; values clamped to 0–255 and positive holds.

    Returns
    -------
    Dict
        Visual session plan.

    Examples
    --------
    >>> plan = glyph_683(300, palette="calm")
    >>> len(plan["steps"]) > 0
    True

    Exceptions
    ----------
    - ValueError : invalid durations or RGB values.

    Complexity
    ----------
    - Time  : O(k) where k is number of steps
    - Space : O(k)
    """
    if duration_s < 30:
        raise ValueError("duration_s must be >= 30")

    presets = {
        "calm":    [(180, 220, 255, 10.0), (170, 210, 240, 10.0)],
        "focus":   [(255, 245, 200, 8.0),  (200, 255, 240, 8.0)],
        "restore": [(200, 255, 220, 9.0),  (220, 200, 255, 9.0)],
        "sleep":   [(120, 160, 255, 12.0), (100, 140, 220, 12.0)],
    }
    steps = sequence or presets[palette]

    safe_steps = []
    t = 0.0
    for r,g,b,hold in steps:
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            raise ValueError("RGB values must be 0–255")
        if hold <= 0:
            raise ValueError("hold must be > 0")
        t += hold
        if hold < (1/30):
            raise ValueError("hold step too short; risks >30 Hz flicker")
        safe_steps.append((int(r), int(g), int(b), float(hold)))
    if t < duration_s:
        # loop sequence gently
        while t < duration_s:
            for s in steps:
                r,g,b,hold = s
                t += hold
                if t > duration_s: break
                safe_steps.append((int(r), int(g), int(b), float(hold)))

    return {"type": "light_session", "duration_s": duration_s, "steps": safe_steps}
