# glyph_632.py — GENTLE_AIRFLOW_CONTROL
# -----------------------------------------------------------------------------
# ID:            632
# Pack:          Pack 007 (601–700)
# Name:          GENTLE_AIRFLOW_CONTROL
# Class:         environmental_care
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Dict

def glyph_632(temp_delta_c: float, occupant_sensitivity: float, *,
              rpm_max: float = 1200.0) -> Dict[str, float]:
    """
    GENTLE_AIRFLOW_CONTROL — compute fan RPM for comfort without startle.

    Overview
    --------
    Higher temperature delta increases RPM; occupant sensitivity reduces it.

    Parameters
    ----------
    temp_delta_c : float
    occupant_sensitivity : float
        In [0,1]; 1 = very sensitive.
    rpm_max : float, optional (default: ``1200.0``)

    Returns
    -------
    Dict[str, float]
        {'rpm': float}

    Examples
    --------
    >>> glyph_632(3.0, 1.0)['rpm'] <= 1200.0
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    sens = max(0.0, min(1.0, occupant_sensitivity))
    gain = 0.4 + 0.6*(1.0 - sens)
    rpm = max(0.0, min(rpm_max, gain * 600.0 * max(0.0, temp_delta_c)))
    return {"rpm": rpm}
