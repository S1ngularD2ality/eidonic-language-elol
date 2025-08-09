# glyph_952 – RATE_LIMIT_PROOF_OF_WORK
"""
Rate-Limit with Proof-of-Work (Hashcash-like)

Server issues a challenge; client must find nonce s.t. H(challenge||nonce) has
d leading zero bits.

APIs:
- issue_challenge() -> bytes
- solve(challenge: bytes, difficulty_bits: int) -> int (nonce)
- verify(challenge, nonce, difficulty_bits) -> bool
"""

import os, hashlib

def issue_challenge() -> bytes:
    return os.urandom(32)

def solve(challenge: bytes, difficulty_bits: int) -> int:
    target = 1 << (256 - difficulty_bits)
    nonce = 0
    while True:
        h = int.from_bytes(hashlib.sha3_512(challenge + nonce.to_bytes(8,"big")).digest(), "big")
        if h < target:
            return nonce
        nonce += 1

def verify(challenge: bytes, nonce: int, difficulty_bits: int) -> bool:
    target = 1 << (256 - difficulty_bits)
    h = int.from_bytes(hashlib.sha3_512(challenge + nonce.to_bytes(8,"big")).digest(), "big")
    return h < target
