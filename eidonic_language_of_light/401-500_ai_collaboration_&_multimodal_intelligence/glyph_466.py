# glyph_466.py — Graceful Pause
# -----------------------------------------------------------------------------
# ID:            466
# Pack:          Pack 005 (401–500)
# Name:          Graceful Pause
# Class:         policy
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_466(error_rate: float, *, threshold: float) -> bool:
    """
    Graceful Pause — pause pipeline if error_rate exceeds threshold.

    Overview
    --------
    Returns True when pause should be engaged.

    Parameters
    ----------
    error_rate : float
    threshold  : float

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_466(0.12, threshold=0.1)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    return float(error_rate) > float(threshold)
