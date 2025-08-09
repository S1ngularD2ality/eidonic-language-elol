# glyph_976 – KEY_SPLIT_AND_WRAP
"""
Key Split & Wrap

Splits a symmetric key into two halves; wraps each under a different wrapping
key (e.g., held by separate services). Both halves required to recover.

APIs:
- wrap(master_key, wrapA, wrapB) -> blob
- unwrap(blob, wrapA, wrapB) -> master_key|None
"""

import hashlib, hmac

def _ks(key: bytes, n: int) -> bytes:
    out=b""; ctr=0
    while len(out)<n:
        out += hashlib.blake2b(key + ctr.to_bytes(8,"big"), digest_size=32).digest()
        ctr+=1
    return out[:n]

def wrap(master_key: bytes, wrapA: bytes, wrapB: bytes) -> bytes:
    half = len(master_key)//2
    A = bytes(a ^ b for a,b in zip(master_key[:half], _ks(wrapA, half)))
    B = bytes(a ^ b for a,b in zip(master_key[half:], _ks(wrapB, len(master_key)-half)))
    mac = hmac.new(wrapA+wrapB, A+B, hashlib.blake2b).digest()
    return len(A).to_bytes(4,"big") + A + B + mac

def unwrap(blob: bytes, wrapA: bytes, wrapB: bytes) -> bytes | None:
    half = int.from_bytes(blob[:4],"big")
    off=4
    A = blob[off:off+half]; off+=half
    B = blob[off:-64]
    mac = blob[-64:]
    if not hmac.compare_digest(hmac.new(wrapA+wrapB, A+B, hashlib.blake2b).digest(), mac):
        return None
    left  = bytes(a ^ b for a,b in zip(A, _ks(wrapA, half)))
    right = bytes(a ^ b for a,b in zip(B, _ks(wrapB, len(B))))
    return left + right
