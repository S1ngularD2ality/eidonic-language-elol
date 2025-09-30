# glyph_615.py — AUTO_CHARGE_DOCK
# -----------------------------------------------------------------------------
# ID:            615
# Pack:          Pack 007 (601–700)
# Name:          AUTO_CHARGE_DOCK
# Class:         coordination_comms
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # policy planner; no docking I/O
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_615(battery_pct: float, queue_len: int, *,
              low_thresh: float = 25.0) -> Dict[str, float | bool]:
    """
    AUTO_CHARGE_DOCK — decide when to request docking.

    Returns
    -------
    {'request': bool, 'priority': float}
    """
    b = max(0.0, min(100.0, battery_pct))
    k = 1.0 + max(0, queue_len)
    priority = (100.0 - b) / k
    return {"request": b < low_thresh, "priority": float(priority)}
