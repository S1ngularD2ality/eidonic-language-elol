# glyph_507.py — Intrusion Alert
# -----------------------------------------------------------------------------
# ID:            507
# Pack:          Pack 006 (501–600)
# Name:          Intrusion Alert
# Class:         auth_access_control
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # threshold logic only
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
from typing import Sequence

def glyph_507(failed_logins: Sequence[float], *, window: int, threshold: int) -> bool:
    """
    Intrusion Alert — raise True if last `window` attempts contain >= `threshold` failures.

    Overview
    --------
    Sliding lookback over the tail of the sequence (1=failure, 0=success).

    Parameters
    ----------
    failed_logins : Sequence[float]
    window        : int
    threshold     : int

    Returns
    -------
    bool

    Examples
    --------
    >>> glyph_507([0,1,1,0,1], window=3, threshold=2)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(window)
    - Space : O(1)
    """
    tail = failed_logins[-window:] if window > 0 else failed_logins
    return sum(1 for x in tail if float(x) != 0.0) >= threshold
