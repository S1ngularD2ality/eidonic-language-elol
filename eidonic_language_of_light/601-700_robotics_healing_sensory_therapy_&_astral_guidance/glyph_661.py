# glyph_661.py — SAFE_RETRACT_MECHANISM
# -----------------------------------------------------------------------------
# ID:            661
# Pack:          Pack 007 (601–700)
# Name:          SAFE_RETRACT_MECHANISM
# Class:         manipulation_safety
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_661(extension_m: float, min_clear_m: float, *,
              retract_rate_mps: float = 0.05) -> Dict[str, float | bool]:
    """
    SAFE_RETRACT_MECHANISM — compute a gentle, bounded retract plan.

    Overview
    --------
    For a linear actuator/tool at `extension_m`, plan a retract distance and
    time that guarantees at least `min_clear_m` clearance from hazards using a
    capped rate. Pure algebra; no device I/O.

    Parameters
    ----------
    extension_m : float
        Current extension (m), >= 0.
    min_clear_m : float
        Required final clearance (m), >= 0.
    retract_rate_mps : float, optional (default: ``0.05``)
        Max retract speed (m/s).

    Returns
    -------
    {'distance_m': float, 'time_s': float, 'ok': bool}

    Examples
    --------
    >>> out = glyph_661(0.20, 0.05, retract_rate_mps=0.1)
    >>> out['ok'] and out['distance_m'] >= 0.15
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    ext = max(0.0, extension_m)
    need = max(0.0, min_clear_m)
    dist = max(0.0, ext - need)
    rate = max(1e-6, retract_rate_mps)
    return {"distance_m": dist, "time_s": dist / rate, "ok": ext >= need}
