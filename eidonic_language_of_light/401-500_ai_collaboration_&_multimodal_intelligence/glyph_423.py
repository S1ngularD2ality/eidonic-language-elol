# glyph_423.py — Sensor Translator
# -----------------------------------------------------------------------------
# ID:            423
# Pack:          Pack 005 (401–500)
# Name:          Sensor Translator
# Class:         translator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Mapping, Dict

def glyph_423(packet: Mapping[str, float], mapping: Mapping[str, str]) -> Dict[str, float]:
    """
    Sensor Translator — rename sensor channels via mapping.

    Overview
    --------
    Produces a new dict with keys remapped by ``mapping``; unknown keys pass through.

    Parameters
    ----------
    packet : Mapping[str, float]
    mapping : Mapping[str, str]

    Returns
    -------
    Dict[str, float]

    Examples
    --------
    >>> glyph_423({"ax":1.0,"ay":2.0}, {"ax":"accel_x"})
    {'accel_x': 1.0, 'ay': 2.0}

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(k)
    - Space : O(k)
    """
    out = {}
    for k, v in packet.items():
        out[mapping.get(k, k)] = float(v)
    return out
