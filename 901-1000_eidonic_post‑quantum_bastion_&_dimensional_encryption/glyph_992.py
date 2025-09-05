# glyph_992 – PCR_PROCESS_CHECK
"""
Process Code Region Integrity (PCR-like)

Hashes a list of loaded module byte blobs and produces a PCR-like digest.
Store expected digests and compare at runtime.

APIs:
- pcr(modules: list[bytes]) -> bytes
"""

import hashlib
from typing import List

def pcr(modules: List[bytes]) -> bytes:
    h = hashlib.blake2b(digest_size=32)
    for m in modules:
        h.update(len(m).to_bytes(8, "big")); h.update(m)
    return h.digest()
