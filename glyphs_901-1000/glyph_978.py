# glyph_978 – OBLIVIOUS_SET_MEMBERSHIP
"""
Oblivious Set Membership (PSI-style Sketch)

Client proves/learns whether x is in Server's set without revealing x or the set,
via hashed tokens + Bloom filter. Privacy depends on hash & salt secrecy.

APIs:
- server_prepare(set_items, salt)->Bloom filter (bit array)
- client_query(x, salt)->token; server_check(bloom, token)->bool
"""

import hashlib
from typing import Iterable

def _H(x: bytes) -> bytes:
    return hashlib.blake2b(x, digest_size=16).digest()

def server_prepare(items: Iterable[bytes], salt: bytes, m_bits: int=1<<20, k: int=7) -> bytearray:
    bits = bytearray(m_bits//8)
    for it in items:
        seed = _H(salt + it)
        for i in range(k):
            h = _H(seed + i.to_bytes(1,"big"))
            idx = int.from_bytes(h, "big") % m_bits
            bits[idx//8] |= (1 << (idx % 8))
    return bits

def client_query(x: bytes, salt: bytes, k: int=7) -> list[int]:
    seed = _H(salt + x)
    return [int.from_bytes(_H(seed + i.to_bytes(1,"big")), "big") for i in range(k)]

def server_check(bits: bytearray, tokens: list[int], m_bits: int=1<<20) -> bool:
    for t in tokens:
        idx = t % m_bits
        if not (bits[idx//8] & (1 << (idx % 8))):
            return False
    return True
