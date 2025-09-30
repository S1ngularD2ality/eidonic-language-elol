# glyph_643.py — HUMAN_SIGNAL_INTERPRET
# -----------------------------------------------------------------------------
# ID:            643
# Pack:          Pack 007 (601–700)
# Name:          HUMAN_SIGNAL_INTERPRET
# Class:         human_care_ethics
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # symbolic mapping only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_643(signal: Mapping[str, Any]) -> Dict[str, Any]:
    """
    HUMAN_SIGNAL_INTERPRET — map simple human cues to safe action intents.

    Overview
    --------
    Interprets discrete cues such as hand raise, palm stop, beckon, and point.
    Pure rule mapping: outputs intent tokens usable by a higher-level planner.

    Parameters
    ----------
    signal : Mapping[str, Any]
        Expected keys like {'gesture': 'stop|come|point|wait', 'strength': 0..1}.

    Returns
    -------
    {'intent': str, 'confidence': float}

    Examples
    --------
    >>> glyph_643({'gesture':'stop','strength':0.9})['intent']
    'halt'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    g = str(signal.get("gesture", "")).lower()
    s = max(0.0, min(1.0, float(signal.get("strength", 1.0))))
    table = {
        "stop": "halt",
        "wait": "hold",
        "come": "approach",
        "beckon": "approach",
        "point": "orient",
        "thumbs_up": "proceed",
        "ok": "proceed",
    }
    return {"intent": table.get(g, "unknown"), "confidence": s}
