# glyph_667.py — MEDICAL_SCAN_MODE
# -----------------------------------------------------------------------------
# ID:            667
# Pack:          Pack 007 (601–700)
# Name:          MEDICAL_SCAN_MODE
# Class:         human_care_ethics
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # non-diagnostic, etiquette only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_667(context: Mapping[str, Any]) -> Dict[str, Any]:
    """
    MEDICAL_SCAN_MODE — etiquette parameters for non-contact scanning.

    Overview
    --------
    Provides conservative timing and distance based on context flags. Not
    medical advice; policy shaping only.

    Parameters
    ----------
    context : may include {'bedside': bool, 'icu': bool, 'pediatric': bool}

    Returns
    -------
    {'distance_m': float, 'speed_scale': float, 'mode': str}

    Examples
    --------
    >>> glyph_667({'icu': True})['distance_m'] >= 1.0
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    bedside = bool(context.get("bedside", False))
    icu = bool(context.get("icu", False))
    ped = bool(context.get("pediatric", False))
    dist = 0.8 + (0.2 if bedside else 0.0) + (0.2 if ped else 0.0) + (0.2 if icu else 0.0)
    scale = 0.8 if bedside or ped else (0.7 if icu else 1.0)
    mode = "scan_care"
    return {"distance_m": float(dist), "speed_scale": float(scale), "mode": mode}
