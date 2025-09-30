# glyph_668.py — TOOL_SAFETY_CHECK
# -----------------------------------------------------------------------------
# ID:            668
# Pack:          Pack 007 (601–700)
# Name:          TOOL_SAFETY_CHECK
# Class:         safety_gate
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Any, Dict

def glyph_668(tool: Mapping[str, Any], limits: Mapping[str, Any]) -> Dict[str, Any]:
    """
    TOOL_SAFETY_CHECK — validate tool parameters against allowed limits.

    Overview
    --------
    Reads fields like torque_n_m, speed_rps, and tip_temp_c from `tool` and
    ensures they are within `limits`. Returns violations list.

    Parameters
    ----------
    tool   : Mapping[str, Any]
    limits : Mapping[str, Any]  # {'torque_n_m':float,'speed_rps':float,'tip_temp_c':float}

    Returns
    -------
    {'ok': bool, 'violations': List[str]}

    Examples
    --------
    >>> glyph_668({'torque_n_m':2.0}, {'torque_n_m':1.0})['ok']
    False

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(1)
    """
    viol = []
    for k, vmax in limits.items():
        v = float(tool.get(k, 0.0))
        if v > float(vmax):
            viol.append(k)
    return {"ok": len(viol) == 0, "violations": viol}
