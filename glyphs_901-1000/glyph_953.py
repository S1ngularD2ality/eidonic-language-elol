# glyph_953 – TIME_LOCK_PUZZLE_HASHCHAIN
"""
Time-Lock Puzzle (Sequential Hash-Chain)

Encrypt a secret key under a value that requires T sequential hash iterations to derive.
No parallel speedup without breaking hash sequentiality (quantum-resistant in spirit).

APIs:
- lock(seed: bytes, T: int) -> bytes  (returns anchor)
- unlock(seed: bytes, T: int) -> bytes (re-derives anchor)
"""

import hashlib

def lock(seed: bytes, T: int) -> bytes:
    x = seed
    for _ in range(T):
        x = hashlib.blake2b(x, digest_size=32).digest()
    return x

def unlock(seed: bytes, T: int) -> bytes:
    return lock(seed, T)
