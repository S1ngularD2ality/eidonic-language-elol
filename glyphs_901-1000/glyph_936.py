# glyph_936 – MULTIPARTY_COIN_FLIP
"""
Multi-Party Coin Flip (commit-reveal, bias-resistant)

Flow:
1) Each party commits to random r_i with C_i = H(r_i || salt_i)
2) Reveal phase: publish r_i, salt_i; verify C_i
3) Result = H( XOR_i r_i )

APIs:
- commit(r, salt) -> C
- verify_commit(r, salt, C) -> bool
- result(values: List[bytes]) -> bytes
"""

import os, hashlib, hmac
from typing import List

def commit(r: bytes, salt: bytes) -> bytes:
    return hmac.new(salt, r, hashlib.blake2b).digest()

def verify_commit(r: bytes, salt: bytes, C: bytes) -> bool:
    return hmac.compare_digest(commit(r, salt), C)

def result(values: List[bytes]) -> bytes:
    x = bytearray(32)
    for v in values:
        h = hashlib.blake2b(v, digest_size=32).digest()
        x = bytearray(a ^ b for a, b in zip(x, h))
    return bytes(x)
