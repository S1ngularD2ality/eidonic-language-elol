# glyph_649.py — MEDICAL_ASSIST_MODE
# -----------------------------------------------------------------------------
# ID:            649
# Pack:          Pack 007 (601–700)
# Name:          MEDICAL_ASSIST_MODE
# Class:         human_care_ethics
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # policy only; not medical advice
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_649(vitals: Mapping[str, Any]) -> Dict[str, Any]:
    """
    MEDICAL_ASSIST_MODE — triage-style etiquette cues from coarse vitals.

    Overview
    --------
    Non-diagnostic policy mapping: guides motion & signaling intensity.

    Parameters
    ----------
    vitals : {'hr': float, 'spo2': float, 'resp': float}

    Returns
    -------
    {'mode': 'green'|'yellow'|'red', 'signal_intensity': float}

    Examples
    --------
    >>> glyph_649({'hr':110,'spo2':89,'resp':28})['mode']
    'red'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    hr = float(vitals.get("hr", 70.0))
    spo2 = float(vitals.get("spo2", 98.0))
    resp = float(vitals.get("resp", 14.0))
    red = (hr > 120) or (spo2 < 90) or (resp > 28)
    yellow = (90 < hr <= 120) or (90 <= spo2 < 94) or (20 < resp <= 28)
    if red:
        return {"mode": "red", "signal_intensity": 1.0}
    if yellow:
        return {"mode": "yellow", "signal_intensity": 0.7}
    return {"mode": "green", "signal_intensity": 0.4}
