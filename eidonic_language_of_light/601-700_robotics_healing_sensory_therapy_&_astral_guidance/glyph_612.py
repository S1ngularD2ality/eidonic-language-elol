# glyph_612.py — LOW_LIGHT_MODE
# -----------------------------------------------------------------------------
# ID:            612
# Pack:          Pack 007 (601–700)
# Name:          LOW_LIGHT_MODE
# Class:         environmental_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # policy schedule
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_612(lux: float) -> Dict[str, str | float]:
    """
    LOW_LIGHT_MODE — etiquette for dark environments.

    Returns
    -------
    {'mode': 'dim'|'normal', 'speed_scale': float}
    """
    if lux < 50.0:
        return {"mode": "dim", "speed_scale": 0.5}
    return {"mode": "normal", "speed_scale": 1.0}
