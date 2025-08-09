# glyph_969 – MONOTONIC_COUNTER_SEAL
"""
Monotonic Counter Seal

Binds a counter value to a MAC so it cannot be rolled back without detection.
Use for replay protection, sequence enforcement.

APIs:
- seal(key, counter)->tag
- verify(key, counter, tag)->bool
"""

import hmac, hashlib

def seal(key: bytes, counter: int) -> bytes:
    return hmac.new(key, counter.to_bytes(16, "big"), hashlib.blake2b).digest()

def verify(key: bytes, counter: int, tag: bytes) -> bool:
    return hmac.compare_digest(seal(key, counter), tag)
