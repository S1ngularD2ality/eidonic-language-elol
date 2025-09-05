# glyph_913 – PARALLEL_REALITY_CIPHER
"""
Parallel Reality Cipher

Encrypts by XOR against two independently derived keystreams K1, K2 (orderless).
Decryption requires both streams; omission of either yields random garbage.
"""

import hashlib

def _kstream(key: bytes, length: int) -> bytes:
    out = b""
    ctr = 0
    while len(out) < length:
        block = hashlib.blake2b(key + ctr.to_bytes(8, "big"), digest_size=32).digest()
        out += block
        ctr += 1
    return out[:length]

def prc_encrypt(plain: bytes, key_a: bytes, key_b: bytes) -> bytes:
    s1 = _kstream(hashlib.sha3_512(key_a).digest(), len(plain))
    s2 = _kstream(hashlib.sha3_512(key_b).digest(), len(plain))
    return bytes(p ^ a ^ b for p, a, b in zip(plain, s1, s2))

def prc_decrypt(cipher: bytes, key_a: bytes, key_b: bytes) -> bytes:
    return prc_encrypt(cipher, key_a, key_b)
