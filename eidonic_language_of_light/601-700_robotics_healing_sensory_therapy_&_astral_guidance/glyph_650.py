# glyph_650.py — HEALING_LIGHT_CONTROL
# -----------------------------------------------------------------------------
# ID:            650
# Pack:          Pack 007 (601–700)
# Name:          HEALING_LIGHT_CONTROL
# Class:         etiquette_modes
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # waveform math only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_650(breath_bpm: float, *,
              base_hz: float = 0.1, coupling: float = 0.5) -> Dict[str, float]:
    """
    HEALING_LIGHT_CONTROL — phase-couple pulse rate to human breathing.

    Overview
    --------
    Light pulse frequency = base_hz * (1 - coupling) + (breath_bpm/60) * coupling.

    Parameters
    ----------
    breath_bpm : float
    base_hz : float, optional (default: ``0.1``)
    coupling : float, optional (default: ``0.5``) in [0,1]

    Returns
    -------
    {'pulse_hz': float, 'duty': float}

    Examples
    --------
    >>> glyph_650(6.0)['pulse_hz'] > 0
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    c = max(0.0, min(1.0, coupling))
    pulse = base_hz*(1-c) + (max(0.0, breath_bpm)/60.0)*c
    duty = 0.5
    return {"pulse_hz": float(pulse), "duty": float(duty)}
