# glyph_620.py — ENVIRONMENT_MONITOR
# -----------------------------------------------------------------------------
# ID:            620
# Pack:          Pack 007 (601–700)
# Name:          ENVIRONMENT_MONITOR
# Class:         environmental_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # rule evaluation only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_620(readings: Mapping[str, float], *,
              limits: Mapping[str, Mapping[str, float]]) -> Dict[str, Any]:
    """
    ENVIRONMENT_MONITOR — evaluate sensors against min/max limits.

    Parameters
    ----------
    readings : {'temp': 22.1, 'co2': 500, ...}
    limits   : {'temp': {'min': 18, 'max': 27}, 'co2': {'max': 800}, ...}

    Returns
    -------
    {'ok': bool, 'violations': List[str]}
    """
    vios = []
    for k, v in readings.items():
        rng = limits.get(k, {})
        if 'min' in rng and v < float(rng['min']): vios.append(f"{k}:below")
        if 'max' in rng and v > float(rng['max']): vios.append(f"{k}:above")
    return {"ok": len(vios) == 0, "violations": vios}
