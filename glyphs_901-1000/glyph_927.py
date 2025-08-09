# glyph_927 – DOUBLE_RATCHET_MINI
"""
Mini Double-Ratchet (symmetric-only demo)

Maintains a root key and sends/recv chains with per-message keys.
APIs:
- kdf_root(root, dh_out) -> new_root, ck
- kdf_chain(ck) -> ck', mk
"""

import hashlib
from typing import Tuple

def _H(x: bytes) -> bytes:
    return hashlib.blake2b(x, digest_size=32).digest()

def kdf_root(root: bytes, dh_out: bytes) -> Tuple[bytes, bytes]:
    seed = _H(root + dh_out)
    return _H(seed + b"root"), _H(seed + b"chain")

def kdf_chain(ck: bytes) -> Tuple[bytes, bytes]:
    return _H(ck + b"CK"), _H(ck + b"MK")
