# glyph_475.py — Byzantine Guard
# -----------------------------------------------------------------------------
# ID:            475
# Pack:          Pack 005 (401–500)
# Name:          Byzantine Guard
# Class:         detector
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_475(values: Sequence[float], *, z: float = 3.0) -> bool:
    """
    Byzantine Guard — flag if any value deviates by > z·MAD from median.

    Overview
    --------
    Robust outlier detector using Median Absolute Deviation.

    Parameters
    ----------
    values : Sequence[float]
    z      : float, optional (default: 3.0)

    Returns
    -------
    bool : True if anomaly detected.

    Examples
    --------
    >>> glyph_475([1,1,1,100], z=3)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n log n)
    - Space : O(n)
    """
    if not values:
        return False
    s = sorted(float(v) for v in values)
    m = s[len(s)//2] if len(s)%2 else 0.5*(s[len(s)//2-1]+s[len(s)//2])
    dev = [abs(v - m) for v in s]
    mad = sorted(dev)[len(dev)//2] if len(dev)%2 else 0.5*(sorted(dev)[len(dev)//2-1]+sorted(dev)[len(dev)//2])
    if mad == 0:
        return any(v != m for v in s)
    return any(abs(v - m) > z * mad for v in s)
