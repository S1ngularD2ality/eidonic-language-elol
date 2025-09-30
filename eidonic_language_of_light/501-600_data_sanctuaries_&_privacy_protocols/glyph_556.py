# glyph_556.py — Log Decrypt
# -----------------------------------------------------------------------------
# ID:            556
# Pack:          Pack 006 (501–600)
# Name:          Log Decrypt
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

def glyph_556(cipher: bytes, *, key: bytes, mac: str) -> str:
    """
    Log Decrypt — verify HMAC and restore UTF-8 log content.

    Overview
    --------
    Recomputes `HMAC_SHA256(key, cipher)` and inverts the XOR keystream.

    Parameters
    ----------
    cipher : bytes
        Ciphertext from `glyph_555`.
    key : bytes
        Secret key.
    mac : str
        Expected MAC hex.

    Returns
    -------
    str
        Plaintext log string.

    Examples
    --------
    >>> c, m = glyph_555("log", key=b"k")
    >>> glyph_556(c, key=b"k", mac=m)
    'log'
    """
    if hmac.new(key, cipher, hashlib.sha256).hexdigest() != mac:
        raise ValueError("MAC verification failed")
    stream = hashlib.sha256(key).digest()
    out = bytearray(cipher)
    for i in range(len(out)):
        out[i] ^= stream[i % len(stream)]
    return bytes(out).decode("utf-8")
