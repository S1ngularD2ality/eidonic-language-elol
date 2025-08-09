# glyph_925 – WOTS_LITE
"""
WOTS-lite (Winternitz-style) One-Time Signature – Simplified

Parameters:
- n = 32 bytes, w = 16 (nibbles). Chain length per nibble: 15.

APIs:
- keygen() -> (sk_parts, pk_parts)
- sign(msg) -> list of chain values at positions given by msg digest nibbles
- verify(msg, sig, pk_parts) -> bool by chaining forward to max

Note: Educational skeleton; not a drop-in for production XMSS/WOTS+.
"""

import os, hashlib
from typing import List, Tuple

n = 32
w = 16
chain_len = w - 1

def _H(x: bytes) -> bytes:
    return hashlib.blake2b(x, digest_size=n).digest()

def _nibbles(d: bytes) -> List[int]:
    out=[]
    for b in d:
        out.append(b >> 4)
        out.append(b & 0x0F)
    return out

def keygen(parts: int = 64) -> Tuple[List[bytes], List[bytes]]:
    sk = [os.urandom(n) for _ in range(parts)]
    pk = []
    for s in sk:
        v = s
        for _ in range(chain_len):
            v = _H(v)
        pk.append(v)
    return sk, pk

def sign(msg: bytes, sk: List[bytes]) -> List[bytes]:
    d = _nibbles(_H(msg))
    sig=[]
    for i, s in enumerate(sk):
        steps = d[i % len(d)]
        v = s
        for _ in range(steps):
            v = _H(v)
        sig.append(v)
    return sig

def verify(msg: bytes, sig: List[bytes], pk: List[bytes]) -> bool:
    d = _nibbles(_H(msg))
    for i, v in enumerate(sig):
        steps = chain_len - d[i % len(d)]
        for _ in range(steps):
            v = _H(v)
        if v != pk[i]:
            return False
    return True
