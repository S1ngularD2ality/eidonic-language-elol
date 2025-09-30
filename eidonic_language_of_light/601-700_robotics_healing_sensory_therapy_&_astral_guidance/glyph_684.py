# glyph_684.py — BREATH_SYNC_GUIDE
# -----------------------------------------------------------------------------
# ID:            684
# Pack:          Pack 007 (601–700)
# Name:          BREATH_SYNC_GUIDE
# Class:         therapy.breath
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict, List, Literal

Pattern = Literal["box", "478", "coherent"]

def glyph_684(cycles: int = 10, pattern: Pattern = "box", pace_s: float = 1.0) -> Dict:
    """
    BREATH_SYNC_GUIDE — generate a timed inhale/hold/exhale/hold cue plan.

    Overview
    --------
    Emits seconds per phase for common patterns:
    - **box**:      4-4-4-4
    - **478**:      4-7-8-0
    - **coherent**: 5-0-5-0 (≈6 breaths/min)

    Parameters
    ----------
    cycles : int, optional
        Number of breath cycles (>= 1).
    pattern : {"box","478","coherent"}
        Pattern selection.
    pace_s : float, optional
        Scalar multiplier for all segments.

    Returns
    -------
    Dict
        Breath plan with list of phases.

    Examples
    --------
    >>> plan = glyph_684(3, "coherent")
    >>> plan["phases"][0]
    {"inhale": 5.0, "hold1": 0.0, "exhale": 5.0, "hold2": 0.0}

    Exceptions
    ----------
    - ValueError : invalid cycles or pace.

    Complexity
    ----------
    - Time  : O(cycles)
    - Space : O(cycles)
    """
    if cycles < 1:
        raise ValueError("cycles must be >= 1")
    if pace_s <= 0:
        raise ValueError("pace_s must be > 0")

    base = {
        "box":      (4, 4, 4, 4),
        "478":      (4, 7, 8, 0),
        "coherent": (5, 0, 5, 0),
    }[pattern]
    phases: List[Dict[str, float]] = []
    for _ in range(cycles):
        inhale, hold1, exhale, hold2 = [x * pace_s for x in base]
        phases.append({"inhale": inhale, "hold1": hold1, "exhale": exhale, "hold2": hold2})
    return {"type": "breath_session", "pattern": pattern, "cycles": cycles, "phases": phases}
