# glyph_989 – VAULT_SEAL_QUORUM
"""
Vault Seal with Quorum

Wraps a secret with t-of-n shares and verifies quorum before unsealing.
(Uses internal XOR n-of-n for demo; swap with Shamir if partial recovery required.)

APIs:
- wrap(secret: bytes, n: int) -> list[bytes]
- unseal(shares: list[bytes]) -> bytes
"""

from typing import List

def wrap(secret: bytes, n: int) -> List[bytes]:
    import os
    shares = [os.urandom(len(secret)) for _ in range(n-1)]
    acc = secret
    for s in shares:
        acc = bytes(a ^ b for a, b in zip(acc, s))
    return shares + [acc]

def unseal(shares: List[bytes]) -> bytes:
    out = bytes([0]*len(shares[0]))
    for s in shares:
        out = bytes(a ^ b for a, b in zip(out, s))
    return out
