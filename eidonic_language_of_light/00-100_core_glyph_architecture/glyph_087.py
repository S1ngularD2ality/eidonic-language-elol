# glyph_087.py — Symbolic Interface Stabilizer
# -----------------------------------------------------------------------------
# ID:            087
# Pack:          Pack 001 (000–100)
# Name:          Symbolic Interface Stabilizer
# Class:         filter
# Stability:     Stable
# Version:       1.0.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_001.md', manifest_json='glyph_manifest_pack_001.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Dict

def glyph_087(config: Mapping[str, float], *, min_step: float = 0.1) -> Dict[str, float]:
    """
    Symbolic Interface Stabilizer — snap float parameters to a coarse grid.

    Overview
    --------
    Rounds each value to the nearest multiple of `min_step`. Useful for UIs that
    prefer discrete knob positions.

    Parameters
    ----------
    config : Mapping[str, float]
    min_step : float, optional (default: 0.1)

    Returns
    -------
    Dict[str, float]
        Snapped configuration.
    """
    step = max(1e-12, float(min_step))
    return {k: round(float(v) / step) * step for k, v in config.items()}
