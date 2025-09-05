# glyph_990 – RANDOM_BEACON_CHAIN
"""
Randomness Beacon (Hash-Chain Verified)

Emits time-indexed randomness values derived by hashing forward from a public seed.
Verifiers recompute expected value for slot t and compare.

APIs:
- class Beacon(seed: bytes).value(t:int)->bytes
- verify(seed, t, value)->bool
"""

import hashlib

def _H(x: bytes) -> bytes:
    return hashlib.blake2b(x, digest_size=32).digest()

class Beacon:
    def __init__(self, seed: bytes):
        self.seed = seed

    def value(self, t: int) -> bytes:
        v = self.seed
        for _ in range(t):
            v = _H(v)
        return v

def verify(seed: bytes, t: int, value: bytes) -> bool:
    v = seed
    for _ in range(t):
        v = _H(v)
    return v == value
