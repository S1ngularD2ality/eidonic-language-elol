# glyph_923 – HASH_CHAIN_OTP
"""
Hash-Chain One-Time Passwords (Lamport-style)

- Server stores anchor = H^N(seed)
- Client proves step i with token = H^(N-i)(seed)
- Server verifies H^i(token) == anchor, then advances window.

APIs:
- make_seed() -> bytes
- derive_anchor(seed: bytes, N: int) -> bytes
- token_at(seed: bytes, i: int, N: int) -> bytes
"""

import os, hashlib

def _H(x: bytes) -> bytes:
    return hashlib.blake2b(x, digest_size=32).digest()

def make_seed() -> bytes:
    return os.urandom(32)

def derive_anchor(seed: bytes, N: int) -> bytes:
    t = seed
    for _ in range(N):
        t = _H(t)
    return t

def token_at(seed: bytes, i: int, N: int) -> bytes:
    assert 0 <= i <= N
    t = seed
    for _ in range(N - i):
        t = _H(t)
    return t
