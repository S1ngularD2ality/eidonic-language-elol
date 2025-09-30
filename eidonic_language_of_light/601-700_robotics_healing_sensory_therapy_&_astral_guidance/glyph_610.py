# glyph_610.py — ENERGY_CONSERVE_MODE
# -----------------------------------------------------------------------------
# ID:            610
# Pack:          Pack 007 (601–700)
# Name:          ENERGY_CONSERVE_MODE
# Class:         metrics_costing
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # budget policy
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_610(battery_pct: float, eta_minutes: float) -> Dict[str, float | str]:
    """
    ENERGY_CONSERVE_MODE — compute duty scaling under energy constraints.

    Returns
    -------
    {'scale': float, 'mode': str}
    """
    b = max(0.0, min(100.0, battery_pct))
    e = max(0.0, eta_minutes)
    scale = 0.5 if b < 20.0 or e > 60.0 else (0.8 if b < 40.0 or e > 30.0 else 1.0)
    mode = "reserve" if scale <= 0.5 else ("thrifty" if scale < 1.0 else "normal")
    return {"scale": float(scale), "mode": mode}
