# glyph_458.py — Retry Oracle
# -----------------------------------------------------------------------------
# ID:            458
# Pack:          Pack 005 (401–500)
# Name:          Retry Oracle
# Class:         policy
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_458(attempt: int, *, max_retries: int = 3) -> bool:
    """
    Retry Oracle — return True if another retry is allowed.

    Overview
    --------
    Allows attempts 0..max_retries-1.

    Parameters
    ----------
    attempt     : int
    max_retries : int, optional (default: 3)

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_458(2, max_retries=3)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    return int(attempt) < int(max_retries)
