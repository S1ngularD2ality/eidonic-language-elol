# glyph_626.py — ENVIRONMENTAL_HAZARD_ALERT
# -----------------------------------------------------------------------------
# ID:            626
# Pack:          Pack 007 (601–700)
# Name:          ENVIRONMENTAL_HAZARD_ALERT
# Class:         environmental_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_626(readings: Mapping[str, float], limits: Mapping[str, Mapping[str, float]]) -> Dict[str, Any]:
    """
    ENVIRONMENTAL_HAZARD_ALERT — evaluate environment for breaches.

    Overview
    --------
    Compares sensor map against min/max thresholds and lists alerts.

    Parameters
    ----------
    readings : Mapping[str, float]
    limits   : Mapping[str, {'min'?: float, 'max'?: float}]

    Returns
    -------
    Dict[str, Any]
        {'ok': bool, 'alerts': List[str]}

    Examples
    --------
    >>> glyph_626({'co2':900}, {'co2':{'max':800}})['ok']
    False

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    alerts = []
    for k, v in readings.items():
        rng = limits.get(k, {})
        if 'min' in rng and v < float(rng['min']): alerts.append(f"{k}:below")
        if 'max' in rng and v > float(rng['max']): alerts.append(f"{k}:above")
    return {"ok": len(alerts) == 0, "alerts": alerts}
