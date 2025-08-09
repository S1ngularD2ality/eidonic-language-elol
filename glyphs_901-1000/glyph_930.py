# glyph_930 – HONEY_ENCRYPTION_DEMO
"""
Honey Encryption – Dictionary-Confounded Demo

Encrypt such that *any* key yields a plausible plaintext from a message space.
Here we map keys to dictionary entries; the wrong key returns a believable fake.

APIs:
- he_encrypt(msg: str, dict_space: List[str], key: bytes) -> ciphertext
- he_decrypt(ciphertext, dict_space, key) -> str (true or plausible)
"""

import hashlib, hmac
from typing import List

def _idx(key: bytes, n: int) -> int:
    d = hashlib.blake2b(key, digest_size=8).digest()
    return int.from_bytes(d, "big") % n

def he_encrypt(msg: str, dict_space: List[str], key: bytes) -> bytes:
    i = dict_space.index(msg)
    j = _idx(key, len(dict_space))
    # store offset so only right key maps back to msg
    off = (i - j) % len(dict_space)
    mac = hmac.new(key, off.to_bytes(4, "big"), hashlib.blake2b).digest()
    return off.to_bytes(4, "big") + mac

def he_decrypt(ct: bytes, dict_space: List[str], key: bytes) -> str:
    off = int.from_bytes(ct[:4], "big")
    j = _idx(key, len(dict_space))
    guess = (off + j) % len(dict_space)
    return dict_space[guess]
