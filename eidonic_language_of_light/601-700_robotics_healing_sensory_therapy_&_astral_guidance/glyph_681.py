# glyph_681.py — SOUND_FREQUENCY_HEAL
# -----------------------------------------------------------------------------
# ID:            681
# Pack:          Pack 007 (601–700)
# Name:          SOUND_FREQUENCY_HEAL
# Class:         therapy.audio
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from __future__ import annotations
from typing import Dict, List, Literal, Tuple

Profile = Literal["calm", "focus", "restore", "sleep"]

def glyph_681(duration_s: int,
              profile: Profile = "calm",
              base_hz: float = 432.0,
              layers: List[Tuple[float, float]] | None = None) -> Dict:
    """
    SOUND_FREQUENCY_HEAL — create a safe, parameterized audio session plan.

    Overview
    --------
    Returns a **pure plan** for therapeutic tones (no I/O). Frequencies are bounded
    to humane ranges (20–20000 Hz), envelopes remain gentle, and output is a JSON-like
    spec suitable for any offline audio renderer.

    Parameters
    ----------
    duration_s : int
        Total session length in seconds (>= 30).
    profile : {"calm","focus","restore","sleep"}, optional
        Curated preset shaping envelopes and partials.
    base_hz : float, optional
        Fundamental frequency (safe-bounded).
    layers : List[Tuple[float, float]], optional
        Additional (freq, gain) partials, gain in [0..1].

    Returns
    -------
    Dict
        Session plan with timeline, envelopes, and partial layers.

    Examples
    --------
    >>> plan = glyph_681(600, profile="restore", base_hz=432.0)
    >>> plan["safety"]["freq_range"]
    [20.0, 20000.0]

    Exceptions
    ----------
    - ValueError : invalid duration or frequency/gain values.

    Complexity
    ----------
    - Time  : O(n) where n is number of timeline keyframes
    - Space : O(n)
    """
    if duration_s < 30:
        raise ValueError("duration_s must be >= 30")
    if not (20.0 <= base_hz <= 20000.0):
        raise ValueError("base_hz out of safe audible range")
    layers = layers or [(base_hz, 0.8), (base_hz*2, 0.2)]
    for f, g in layers:
        if not (20.0 <= float(f) <= 20000.0):
            raise ValueError("layer frequency out of range 20–20000 Hz")
        if not (0.0 <= float(g) <= 1.0):
            raise ValueError("layer gain must be in [0,1]")

    env = {
        "calm":    dict(attack=8.0,  decay=4.0,  sustain=0.7, release=12.0, wobble_hz=0.2),
        "focus":   dict(attack=2.0,  decay=1.0,  sustain=0.9, release=2.0,  wobble_hz=0.1),
        "restore": dict(attack=6.0,  decay=3.0,  sustain=0.8, release=10.0, wobble_hz=0.15),
        "sleep":   dict(attack=12.0, decay=8.0,  sustain=0.6, release=20.0, wobble_hz=0.05),
    }[profile]

    keyframes = [
        {"t": 0,                   "gain": 0.0},
        {"t": env["attack"],       "gain": env["sustain"]},
        {"t": max(0, duration_s - env["release"]), "gain": env["sustain"]},
        {"t": duration_s,          "gain": 0.0},
    ]

    return {
        "type": "sound_session",
        "profile": profile,
        "duration_s": duration_s,
        "partials": [{"freq_hz": float(f), "gain": float(g)} for f, g in layers],
        "envelope": env,
        "timeline": keyframes,
        "safety": {"freq_range": [20.0, 20000.0], "max_gain": 1.0},
        "notes": "Render externally; respect user consent and volume comfort."
    }
