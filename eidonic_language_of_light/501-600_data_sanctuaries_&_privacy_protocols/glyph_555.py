# glyph_555.py — Log Encrypt
# -----------------------------------------------------------------------------
# ID:            555
# Pack:          Pack 006 (501–600)
# Name:          Log Encrypt
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import hashlib, hmac
from typing import Tuple

def glyph_555(text: str, *, key: bytes) -> Tuple[bytes, str]:
    """
    Log Encrypt — line-stable XOR stream + HMAC sealing for plaintext logs.

    Overview
    --------
    Applies a SHA-256-derived XOR keystream to UTF-8 log text and returns
    `(cipher, mac_hex)`. Pair with `glyph_556` to restore.

    Parameters
    ----------
    text : str
        Log content.
    key : bytes
        Secret key.

    Returns
    -------
    (bytes, str)
        Ciphertext and HMAC-SHA256 hex.

    Examples
    --------
    >>> c, m = glyph_555("x", key=b"k")
    >>> glyph_556(c, key=b"k", mac=m)
    'x'
    """
    data = text.encode("utf-8")
    stream = hashlib.sha256(key).digest()
    out = bytearray(data)
    for i in range(len(out)):
        out[i] ^= stream[i % len(stream)]
    mac = hmac.new(key, bytes(out), hashlib.sha256).hexdigest()
    return bytes(out), mac
