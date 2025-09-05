# glyph_934 – INTEGRITY_TRIPWIRE
"""
Integrity Tripwire

Maintains rolling hash over critical files/bytes; detects modification.
APIs:
- fingerprint(chunks: List[bytes]) -> bytes
- changed(prev_fp, chunks) -> bool
"""

import hashlib
from typing import List

def fingerprint(chunks: List[bytes]) -> bytes:
    h = hashlib.blake2b(digest_size=32)
    for c in chunks:
        h.update(len(c).to_bytes(8, "big")); h.update(c)
    return h.digest()

def changed(prev_fp: bytes, chunks: List[bytes]) -> bool:
    return fingerprint(chunks) != prev_fp
