# glyph_527.py — Two Factor Verify
# -----------------------------------------------------------------------------
# ID:            527
# Pack:          Pack 006 (501–600)
# Name:          Two Factor Verify
# Class:         auth_mfa
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # windowed verification
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
def glyph_527(secret: bytes, code: str, *, unix_time: int, step: int = 30, skew: int = 1, digits: int = 6) -> bool:
    """
    Two Factor Verify — check a code within ±`skew` time steps.

    Overview
    --------
    Recomputes codes over the tolerated window and compares for equality.

    Parameters
    ----------
    secret    : bytes
    code      : str
    unix_time : int
    step      : int
    skew      : int
    digits    : int

    Returns
    -------
    bool

    Examples
    --------
    >>> c = glyph_526(b'k', unix_time=90, step=30)
    >>> glyph_527(b'k', c, unix_time=91, step=30, skew=1)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(skew)
    - Space : O(1)
    """
    for k in range(-int(skew), int(skew) + 1):
        if glyph_526(secret, unix_time=unix_time + k*step, step=step, digits=digits) == code:  # type: ignore
            return True
    return False
