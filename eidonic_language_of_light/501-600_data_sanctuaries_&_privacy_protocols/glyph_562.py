# glyph_562.py — Sign Message
# -----------------------------------------------------------------------------
# ID:            562
# Pack:          Pack 006 (501–600)
# Name:          Sign Message
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
from typing import bytes as _bytes

def glyph_562(message: _bytes, *, key: _bytes) -> _bytes:
    """
    Sign Message — compute HMAC-SHA256 over message.

    Parameters
    ----------
    message : bytes
    key     : bytes

    Returns
    -------
    bytes : raw 32-byte tag

    Examples
    --------
    >>> t = glyph_562(b"x", key=b"k"); len(t) == 32
    True
    """
    return hmac.new(key, message, hashlib.sha256).digest()
