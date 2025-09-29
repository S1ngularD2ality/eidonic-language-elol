# glyph_487.py — Link Health
# -----------------------------------------------------------------------------
# ID:            487
# Pack:          Pack 005 (401–500)
# Name:          Link Health
# Class:         monitor
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_487(rtts_ms: Sequence[float], loss_pct: float, *, max_rtt_ms: float, max_loss_pct: float) -> bool:
    """
    Link Health — True if median RTT and loss are within thresholds.

    Overview
    --------
    Deterministic median for even counts uses mean of middle pair.

    Parameters
    ----------
    rtts_ms      : Sequence[float]
    loss_pct     : float
    max_rtt_ms   : float
    max_loss_pct : float

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_487([10,20,30], 1.0, max_rtt_ms=25, max_loss_pct=2.0)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(1)
    """
    s = sorted(float(v) for v in rtts_ms) if rtts_ms else []
    if not s:
        return False
    n = len(s)
    med = s[n//2] if n % 2 else 0.5*(s[n//2-1] + s[n//2])
    return (med <= float(max_rtt_ms)) and (float(loss_pct) <= float(max_loss_pct))
