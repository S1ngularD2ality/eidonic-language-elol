# glyph_608.py — GRIP_STRENGTH_MODULATION
# -----------------------------------------------------------------------------
# ID:            608
# Pack:          Pack 007 (601–700)
# Name:          GRIP_STRENGTH_MODULATION
# Class:         manipulation_gentle
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # algebraic envelope; no actuators
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_608(object_mass_kg: float, fragility: float, *,
              max_force_n: float = 20.0) -> Dict[str, float]:
    """
    GRIP_STRENGTH_MODULATION — safe force envelope from mass & fragility.

    Parameters
    ----------
    object_mass_kg : float
    fragility : float
        In [0,1]; 1 = ultra-fragile.

    Returns
    -------
    {'f_target_n': float}
    """
    fragility = max(0.0, min(1.0, fragility))
    base = 9.81 * max(0.0, object_mass_kg)
    f = min(max_force_n, base * (1.0 - 0.7*fragility) + 1.0)
    return {"f_target_n": float(max(0.5, f))}
