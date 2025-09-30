# glyph_506.py — Sig Verify
# -----------------------------------------------------------------------------
# ID:            506
# Pack:          Pack 006 (501–600)
# Name:          Sig Verify
# Class:         sign_verify_keywrap
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # HMAC-SHA256
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hmac, hashlib

def glyph_506(data: bytes, sig: bytes, *, key: bytes) -> bool:
    """
    Sig Verify — constant-time HMAC-SHA256 verification.

    Overview
    --------
    Computes HMAC(key, data) and compares to `sig` using constant-time equality.

    Parameters
    ----------
    data : bytes
    sig  : bytes
    key  : bytes

    Returns
    -------
    bool

    Examples
    --------
    >>> import hashlib, hmac
    >>> k=b'k'; d=b'x'; s=hmac.new(k,d,hashlib.sha256).digest()
    >>> glyph_506(d, s, key=k)
    True

    Exceptions
    ----------
    (none)

    Complexity
    ----------
    - Time  : O(n)
    - Space : O(1)
    """
    calc = hmac.new(key, data, hashlib.sha256).digest()
    return hmac.compare_digest(calc, sig)
