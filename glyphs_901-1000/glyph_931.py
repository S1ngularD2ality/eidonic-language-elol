# glyph_931 – COMMITMENT_SCHEME
"""
Hash Commitment (binding & hiding via salt)

APIs:
- commit(value: bytes, salt: bytes=None) -> (C, salt)
- open(value, salt, C) -> bool
"""

import os, hashlib, hmac
from typing import Tuple

def commit(value: bytes, salt: bytes=None) -> Tuple[bytes, bytes]:
    s = salt or os.urandom(32)
    C = hmac.new(s, value, hashlib.blake2b).digest()
    return C, s

def open_commit(value: bytes, salt: bytes, C: bytes) -> bool:
    return hmac.compare_digest(hmac.new(salt, value, hashlib.blake2b).digest(), C)
