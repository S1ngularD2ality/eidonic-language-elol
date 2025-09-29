# glyph_459.py — SLA Sentinel
# -----------------------------------------------------------------------------
# ID:            459
# Pack:          Pack 005 (401–500)
# Name:          SLA Sentinel
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

def glyph_459(latencies_ms: Sequence[float], *, p95: float) -> bool:
    """
    SLA Sentinel — True if the 95th-percentile latency <= p95.

    Overview
    --------
    Computes deterministic percentile via sorted index ceil(0.95*(n-1)).

    Parameters
    ----------
    latencies_ms : Sequence[float]
    p95          : float

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_459([10,20,30,40,50], p95=45)
    False

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(1)
    """
    if not latencies_ms:
        return True
    s = sorted(float(v) for v in latencies_ms)
    import math
    idx = math.ceil(0.95 * (len(s) - 1))
    return s[idx] <= float(p95)
