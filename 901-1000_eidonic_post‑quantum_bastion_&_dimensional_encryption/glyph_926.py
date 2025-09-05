# glyph_926 – KEY_ROTATION_RATCHET
"""
Key Rotation Ratchet (hash ratchet + periodic salt)

- next_key(k) = H(k || epoch_salt)
- Provides forward secrecy for long-lived services.

APIs:
- next_key(cur_key: bytes, epoch: int) -> bytes
"""

import hashlib

def next_key(cur_key: bytes, epoch: int) -> bytes:
    salt = epoch.to_bytes(8, "big")
    return hashlib.blake2b(cur_key + salt, digest_size=32).digest()
