# glyph_640.py — SENSITIVE_MATERIAL_ALERT
# -----------------------------------------------------------------------------
# ID:            640
# Pack:          Pack 007 (601–700)
# Name:          SENSITIVE_MATERIAL_ALERT
# Class:         material_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_640(plan: Mapping[str, Any], material: Mapping[str, Any]) -> Dict[str, Any]:
    """
    SENSITIVE_MATERIAL_ALERT — validate handling plan against material flags.

    Overview
    --------
    Checks plan limits (force, temperature, placement velocity) against material rules.

    Parameters
    ----------
    plan     : Mapping[str, Any]
        Keys like 'max_force_n': float, 'temp_c': float, 'v_place_mps': float
    material : Mapping[str, Any]
        Keys like 'fragile': bool, 'heat_limit_c': float, 'shock_sens': float (0..1)

    Returns
    -------
    Dict[str, Any]
        {'ok': bool, 'violations': List[str]}

    Examples
    --------
    >>> glyph_640({'max_force_n':12,'temp_c':30,'v_place_mps':0.2}, {'fragile':True,'heat_limit_c':40,'shock_sens':0.5})['ok']
    False

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    viol = []
    maxF = float(plan.get("max_force_n", 0.0))
    temp = float(plan.get("temp_c", 0.0))
    v    = float(plan.get("v_place_mps", 0.0))
    if bool(material.get("fragile", False)) and maxF > 10.0:
        viol.append("force")
    if "heat_limit_c" in material and temp > float(material["heat_limit_c"]):
        viol.append("heat")
    sens = max(0.0, min(1.0, float(material.get("shock_sens", 0.5))))
    if v > (0.1 + 0.9*sens):
        viol.append("shock")
    return {"ok": len(violations := viol) == 0, "violations": violations}
