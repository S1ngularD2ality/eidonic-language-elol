# glyph_827 – CHORD_PROGRESS_PHASE
# Map timestamps to 12-tone phase degrees using BPM/offset (music-memory bridge).

import math

def glyph_827(timestamps, bpm: float, offset_sec: float = 0.0):
    """
    timestamps: list[float] seconds
    bpm: beats per minute
    offset_sec: phase offset in seconds
    Returns list[int] degrees 0..11 mapped by beat-phase.
    """
    if bpm <= 0:
        raise ValueError("bpm > 0")
    beat_sec = 60.0 / bpm
    out = []
    golden = (2*math.pi)*(1 - 1/((1 + 5**0.5)/2))  # golden angle
    for t in timestamps:
        phase = ((t + offset_sec) / beat_sec) * 2*math.pi
        degree = int(((phase + golden) % (2*math.pi)) / (2*math.pi) * 12) % 12
        out.append(degree)
    return out
