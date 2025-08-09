# glyph_924 – LAMPORT_OTS
"""
Lamport One-Time Signature (hash-based, one-use only)

- keygen(): 256 pairs of random 32-byte secrets
- sign(msg): reveal one secret from each pair depending on bit of H(msg)
- verify(msg, sig, pub): hash revealed values and compare with pubkeys

APIs:
- keygen() -> (sk: List[Tuple[bytes,bytes]], pk: List[Tuple[bytes,bytes]])
- sign(msg, sk) -> signature: List[bytes]
- verify(msg, sig, pk) -> bool
"""

import os, hashlib
from typing import List, Tuple

def _H(x: bytes) -> bytes:
    return hashlib.blake2b(x, digest_size=32).digest()

def keygen() -> Tuple[List[Tuple[bytes,bytes]], List[Tuple[bytes,bytes]]]:
    sk, pk = [], []
    for _ in range(256):
        a = os.urandom(32); b = os.urandom(32)
        sk.append((a,b))
        pk.append((_H(a), _H(b)))
    return sk, pk

def sign(msg: bytes, sk: List[Tuple[bytes,bytes]]) -> List[bytes]:
    digest = _H(msg)
    bits = ''.join(f'{byte:08b}' for byte in digest)
    assert len(bits) == 256
    sig = []
    for i, bit in enumerate(bits):
        a,b = sk[i]
        sig.append(a if bit == '0' else b)
    return sig

def verify(msg: bytes, sig: List[bytes], pk: List[Tuple[bytes,bytes]]) -> bool:
    digest = _H(msg)
    bits = ''.join(f'{byte:08b}' for byte in digest)
    if len(sig) != 256: return False
    for i, bit in enumerate(bits):
        h = _H(sig[i])
        if bit == '0':
            if h != pk[i][0]: return False
        else:
            if h != pk[i][1]: return False
    return True
