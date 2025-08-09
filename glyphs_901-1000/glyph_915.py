# glyph_915 – CONSCIOUSNESS_CHECK_GATE
"""
Consciousness Check Gate

Challenge–response over a neural/behavioral embedding vector. Server issues
nonce; client returns HMAC(embedding || nonce). No raw biometrics stored.
"""

import os, hmac, hashlib
from typing import Tuple

def ccg_issue() -> bytes:
    return os.urandom(32)

def ccg_sign(embedding: bytes, nonce: bytes) -> bytes:
    key = hashlib.sha3_512(embedding).digest()
    return hmac.new(key, nonce, hashlib.blake2b).digest()

def ccg_verify(stored_embedding_hash: bytes, nonce: bytes, signature: bytes) -> bool:
    key = stored_embedding_hash  # equals sha3(embedding) at enrollment
    ref = hmac.new(key, nonce, hashlib.blake2b).digest()
    return hmac.compare_digest(ref, signature)
