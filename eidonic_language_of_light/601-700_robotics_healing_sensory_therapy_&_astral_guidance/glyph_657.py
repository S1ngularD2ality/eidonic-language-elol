# glyph_657.py — BOT_HEALTH_MONITOR
# -----------------------------------------------------------------------------
# ID:            657
# Pack:          Pack 007 (601–700)
# Name:          BOT_HEALTH_MONITOR
# Class:         metrics_costing
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # aggregation only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_657(metrics: Mapping[str, Any]) -> Dict[str, Any]:
    """
    BOT_HEALTH_MONITOR — combine subsystem scores into a status.

    Overview
    --------
    Weighted sum of normalized metrics: battery, motor_temp, link_quality, memory.

    Parameters
    ----------
    metrics : {'battery':0..1, 'motor_temp':0..1 (inverted), 'link_quality':0..1, 'memory':0..1}

    Returns
    -------
    {'score': float, 'state': 'ok'|'warn'|'crit'}

    Examples
    --------
    >>> glyph_657({'battery':0.2,'motor_temp':0.3,'link_quality':0.4,'memory':0.5})['state']
    'crit'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    b = float(metrics.get("battery", 1.0))
    t = float(metrics.get("motor_temp", 1.0))   # assume already normalized with 1 good, 0 bad
    l = float(metrics.get("link_quality", 1.0))
    m = float(metrics.get("memory", 1.0))
    score = 0.35*b + 0.25*t + 0.25*l + 0.15*m
    state = "crit" if score < 0.35 else ("warn" if score < 0.7 else "ok")
    return {"score": float(score), "state": state}
