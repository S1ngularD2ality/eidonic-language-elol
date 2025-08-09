# glyph_951 – BLOOM_REVOKE_SET
"""
Bloom Filter Revocation Set

Compact structure to test whether an identifier is (probably) revoked.
False positives possible; false negatives not (for inserted items).

APIs:
- class Bloom: add(id_bytes), contains(id_bytes)->bool
"""

import hashlib

class Bloom:
    def __init__(self, m_bits: int = 1<<20, k_hashes: int = 7):
        self.m = m_bits
        self.k = k_hashes
        self.bits = bytearray(self.m // 8)

    def _indexes(self, x: bytes):
        seed = hashlib.blake2b(x, digest_size=32).digest()
        for i in range(self.k):
            h = hashlib.blake2b(seed + i.to_bytes(4,"big"), digest_size=8).digest()
            yield int.from_bytes(h, "big") % self.m

    def add(self, x: bytes):
        for idx in self._indexes(x):
            self.bits[idx//8] |= (1 << (idx % 8))

    def contains(self, x: bytes) -> bool:
        for idx in self._indexes(x):
            if not (self.bits[idx//8] & (1 << (idx % 8))):
                return False
        return True
