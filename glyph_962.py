# glyph_962 – HKDF_BLAKE2
"""
HKDF (BLAKE2b Variant)

Deterministic key derivation from IKM (input keying material) with salt and info.
Suitable for session keys, subkeys, and context binding.

APIs:
- extract(ikm: bytes, salt: bytes=b"") -> prk
- expand(prk: bytes, info: bytes, L: int) -> bytes
"""

import hmac, hashlib

def extract(ikm: bytes, salt: bytes = b"") -> bytes:
    return hmac.new(salt, ikm, hashlib.blake2b).digest()

def expand(prk: bytes, info: bytes, L: int) -> bytes:
    out = b""
    t = b""
    counter = 1
    while len(out) < L:
        t = hmac.new(prk, t + info + bytes([counter]), hashlib.blake2b).digest()
        out += t
        counter += 1
    return out[:L]
