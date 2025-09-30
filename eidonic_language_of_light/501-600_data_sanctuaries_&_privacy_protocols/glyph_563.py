# glyph_563.py — Verify Signature
# -----------------------------------------------------------------------------
# ID:            563
# Pack:          Pack 006 (501–600)
# Name:          Verify Signature
# Class:         sign_verify_keywrap
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-29
# Deterministic: True   # constant-time compare
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hmac, hashlib
from typing import bytes as _bytes

def glyph_563(message: _bytes, tag: _bytes, *, key: _bytes) -> bool:
    """
    Verify Signature — verify HMAC-SHA256 tag.

    Returns
    -------
    bool

    Examples
    --------
    >>> m=b"x"; k=b"k"; ok = glyph_563(m, glyph_562(m, key=k), key=k); ok
    True
    """
    calc = hmac.new(key, message, hashlib.sha256).digest()
    return hmac.compare_digest(calc, tag)
