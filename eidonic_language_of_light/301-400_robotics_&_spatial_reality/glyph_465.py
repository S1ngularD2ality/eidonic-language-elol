# glyph_465.py — Backpressure Valve
# -----------------------------------------------------------------------------
# ID:            465
# Pack:          Pack 005 (401–500)
# Name:          Backpressure Valve
# Class:         regulator
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_465(queue_depth: int, *, hi: int, lo: int) -> float:
    """
    Backpressure Valve — hysteresis throttle coefficient in [0,1].

    Overview
    --------
    Returns 1.0 below `lo`, 0.0 above `hi`, linearly interpolated in between.

    Parameters
    ----------
    queue_depth : int
    hi          : int
    lo          : int

    Returns
    -------
    float

    Examples
    --------
    >>> glyph_465(5, hi=10, lo=2)
    0.7142857142857143

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if hi <= lo:
        return 0.0 if queue_depth >= hi else 1.0
    if queue_depth <= lo:
        return 1.0
    if queue_depth >= hi:
        return 0.0
    return (hi - float(queue_depth)) / (hi - lo)
