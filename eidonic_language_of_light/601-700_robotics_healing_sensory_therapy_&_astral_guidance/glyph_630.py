# glyph_630.py — WATER_SAFETY_SHUTDOWN
# -----------------------------------------------------------------------------
# ID:            630
# Pack:          Pack 007 (601–700)
# Name:          WATER_SAFETY_SHUTDOWN
# Class:         safety_gate
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_007.md', manifest_json='glyph_manifest_pack_007.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_630(moisture_pct: float, *, threshold_pct: float = 5.0) -> bool:
    """
    WATER_SAFETY_SHUTDOWN — return True if shutdown condition met.

    Overview
    --------
    Simple predicate applied to relative moisture percentage.

    Parameters
    ----------
    moisture_pct : float
    threshold_pct : float, optional (default: ``5.0``)

    Returns
    -------
    bool
        True if moisture exceeds threshold.

    Examples
    --------
    >>> glyph_630(6.0)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    return moisture_pct >= threshold_pct
