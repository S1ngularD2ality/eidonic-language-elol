# glyph_422.py — Audio Whisper
# -----------------------------------------------------------------------------
# ID:            422
# Pack:          Pack 005 (401–500)
# Name:          Audio Whisper
# Class:         analyzer
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, List
import math

def glyph_422(samples: Sequence[float], *, frame: int = 400, step: int = 200, silence_db: float = -40.0) -> List[int]:
    """
    Audio Whisper — detect voiced frames via log-RMS.

    Overview
    --------
    Slides a window, computes RMS in dBFS, and flags frames above ``silence_db``.

    Parameters
    ----------
    samples : Sequence[float]
        Mono PCM-like sequence (any scale; relative).
    frame : int, optional
        Window length in samples (default: 400).
    step : int, optional
        Hop size in samples (default: 200).
    silence_db : float, optional
        Threshold in dB (default: -40.0).

    Returns
    -------
    List[int]
        0-based frame indices considered voiced.

    Examples
    --------
    >>> glyph_422([0.0]*1000, frame=100, step=50, silence_db=-80)
    []

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(n/frame)
    """
    if frame <= 0 or step <= 0:
        return []
    out: List[int] = []
    i = 0
    n = len(samples)
    while i + frame <= n:
        seg = samples[i:i+frame]
        rms = (sum(float(v)*float(v) for v in seg) / frame) ** 0.5
        db = 20.0 * math.log10(max(rms, 1e-12))
        if db > float(silence_db):
            out.append(i // step)
        i += step
    return out
