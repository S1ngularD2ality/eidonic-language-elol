# glyph_548.py — Decrypt Dict
# -----------------------------------------------------------------------------
# ID:            548
# Pack:          Pack 006 (501–600)
# Name:          Decrypt Dict
# Class:         transform
# Stability:     Stable
# Version:       1.1.0
# Since:         2025-09-22
# Deterministic: True
# Thread-Safe:   True
# Provenance:    index_md='glyph_index_pack_006.md', manifest_json='glyph_manifest_pack_006.json'
# License:       EIDONIC COMMUNITY LICENSE — NON-COMMERCIAL v1.1 (ECL-NC-1.1)
# -----------------------------------------------------------------------------
import json, hashlib, hmac
from typing import Dict, Any

def glyph_548(cipher: bytes, *, key: bytes, mac: str) -> Dict[str, Any]:
    """
    Decrypt Dict — verify HMAC then invert the XOR stream.

    Overview
    --------
    Validates `HMAC_SHA256(key, cipher) == mac` then restores canonical JSON.

    Parameters
    ----------
    cipher : bytes
        Ciphertext from `glyph_547`.
    key : bytes
        Secret key.
    mac : str
        Expected MAC hex.

    Returns
    -------
    Dict[str, Any]
        Decoded document.

    Examples
    --------
    >>> c, m = glyph_547({"a":2}, key=b"k")
    >>> glyph_548(c, key=b"k", mac=m)["a"]
    2

    Exceptions
    ----------
    - ValueError : if MAC fails or JSON decode fails.

    Complexity
    ----------
    - Time  : O(N)
    - Space : O(N)
    """
    if hmac.new(key, cipher, hashlib.sha256).hexdigest() != mac:
        raise ValueError("MAC verification failed")
    stream = hashlib.sha256(key).digest()
    out = bytearray(cipher)
    for i in range(len(out)):
        out[i] ^= stream[i % len(stream)]
    try:
        return json.loads(out.decode("utf-8"))
    except Exception as e:
        raise ValueError("invalid JSON after decryption") from e
