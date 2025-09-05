# glyph_909 – LIVING_ONE_TIME_PAD
"""
Living One-Time Pad

Generates a one-time pad for immediate XOR encryption; returns ciphertext and a
digest-of-pad for audit (not the pad). Caller MUST transmit pad via out-of-band
ephemeral channel; pad must be destroyed after use.
"""

import os, hashlib
from typing import Tuple

def otp_encrypt(data: bytes) -> Tuple[bytes, bytes]:
    pad = os.urandom(len(data))
    ct  = bytes(a ^ b for a, b in zip(data, pad))
    pad_digest = hashlib.blake2b(pad, digest_size=32).digest()
    # Pad should be wiped by caller after out-of-band delivery
    return ct, pad_digest

def otp_decrypt(ciphertext: bytes, pad: bytes) -> bytes:
    assert len(ciphertext) == len(pad)
    return bytes(a ^ b for a, b in zip(ciphertext, pad))
