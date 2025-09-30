# glyph_526.py — Two Factor Code
# -----------------------------------------------------------------------------
# ID:            526
# Pack:          Pack 006 (501–600)
# Name:          Two Factor Code
# Class:         auth_mfa
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # given secret/time; HMAC-SHA256 TOTP-like
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hmac, hashlib, struct

def glyph_526(secret: bytes, *, unix_time: int, step: int = 30, digits: int = 6) -> str:
    """
    Two Factor Code — TOTP-style code generation (educational HMAC-SHA256).

    Overview
    --------
    Counter = floor(unix_time/step). Dynamic truncation → modulo 10^digits.

    Parameters
    ----------
    secret    : bytes
    unix_time : int
    step      : int, optional (default: 30)
    digits    : int, optional (default: 6)

    Returns
    -------
    str : zero-padded code

    Examples
    --------
    >>> isinstance(glyph_526(b'k', unix_time=0), str)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(1)
    - Space : O(1)
    """
    counter = (unix_time // step)
    mac = hmac.new(secret, struct.pack(">Q", counter), hashlib.sha256).digest()
    off = mac[-1] & 0x0F
    bin_code = ((mac[off] & 0x7F) << 24) | (mac[off+1] << 16) | (mac[off+2] << 8) | mac[off+3]
    return str(bin_code % (10 ** digits)).zfill(digits)
