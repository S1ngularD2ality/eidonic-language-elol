# glyph_904 – SOULBOUND_KEY_GENERATOR
"""
Soulbound Key Generator

Derives keys bound to a person's biometric vector + contextual tag.
Deterministic per (biometric, tag), non-replayable with ephemeral nonce.
"""

import os, hashlib, hmac
from typing import Tuple

def soulbound_key(biometric_vec: bytes, tag: bytes, nonce: bytes = None) -> Tuple[bytes, bytes]:
    """
    Returns (key, used_nonce).
    tag can embed intent/context (e.g., b'vault-unseal@lab-A')
    """
    used_nonce = nonce or os.urandom(32)
    seed = hashlib.sha3_512(biometric_vec + tag + used_nonce).digest()
    key  = hmac.new(seed, b"SOULBOUND", hashlib.blake2b).digest()
    return key, used_nonce
