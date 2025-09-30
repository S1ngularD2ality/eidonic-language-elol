# glyph_645.py — SOFT_CONTACT_SENSOR
# -----------------------------------------------------------------------------
# ID:            645
# Pack:          Pack 007 (601–700)
# Name:          SOFT_CONTACT_SENSOR
# Class:         manipulation_gentle
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # filter & threshold only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence, Dict, Any

def glyph_645(pressure: Sequence[float], *, alpha: float = 0.3,
              contact_threshold: float = 0.8) -> Dict[str, Any]:
    """
    SOFT_CONTACT_SENSOR — smooth pressure stream and flag gentle contact.

    Overview
    --------
    IIR filter on normalized pressure; contact when filtered >= threshold.

    Parameters
    ----------
    pressure : Sequence[float]
        Normalized 0..1.
    alpha : float, optional (default: ``0.3``)
        EMA factor (0..1).
    contact_threshold : float, optional (default: ``0.8``)

    Returns
    -------
    {'filtered': List[float], 'contact': bool, 'last': float}

    Examples
    --------
    >>> glyph_645([0,0.2,0.6,0.9])['contact']
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    a = max(0.0, min(1.0, alpha))
    out = []
    s = 0.0
    for i, v in enumerate(pressure):
        s = float(v) if i == 0 else (a*float(v) + (1-a)*s)
        out.append(s)
    return {"filtered": out, "contact": (out[-1] >= contact_threshold) if out else False, "last": (out[-1] if out else 0.0)}
