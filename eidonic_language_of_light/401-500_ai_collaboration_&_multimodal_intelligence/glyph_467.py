# glyph_467.py — Circuit Breaker
# -----------------------------------------------------------------------------
# ID:            467
# Pack:          Pack 005 (401–500)
# Name:          Circuit Breaker
# Class:         policy
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_005.md', manifest_json='glyph_manifest_pack_005.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_467(failures: int, *, open_after: int) -> str:
    """
    Circuit Breaker — returns 'closed' or 'open' state.

    Overview
    --------
    Opens after `open_after` consecutive failures.

    Parameters
    ----------
    failures   : int
    open_after : int

    Returns
    -------
    str : 'closed' | 'open'

    Examples
    --------
    >>> glyph_467(3, open_after=3)
    'open'

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    return "open" if int(failures) >= int(open_after) else "closed"
