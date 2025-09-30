# glyph_470.py — Hard Quorum
# -----------------------------------------------------------------------------
# ID:            470
# Pack:          Pack 005 (401–500)
# Name:          Hard Quorum
# Class:         consensus
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_470(votes_for: int, total: int, *, threshold: float = 0.5) -> bool:
    """
    Hard Quorum — boolean decision by fractional threshold.

    Overview
    --------
    Returns True if votes_for / total >= threshold (total>0).

    Parameters
    ----------
    votes_for : int
    total     : int
    threshold : float, optional (default: 0.5)

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_470(3, 5, threshold=0.6)
    False

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    if total <= 0:
        return False
    return (float(votes_for) / float(total)) >= float(threshold)
