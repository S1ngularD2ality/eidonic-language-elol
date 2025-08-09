# glyph_985 – THRESHOLD_MAC_AGGREGATOR
"""
Threshold MAC Aggregator

Accepts t-of-n HMAC tags over the same message and validates quorum acceptance.
Use when signatures are overkill and shared secrets are practical.

APIs:
- accept(message: bytes, tags: list[bytes], keys: list[bytes], t: int) -> bool
"""

import hmac, hashlib

def accept(message: bytes, tags: list[bytes], keys: list[bytes], t: int) -> bool:
    ok = 0
    for k, tag in zip(keys, tags):
        ref = hmac.new(k, message, hashlib.blake2b).digest()
        ok += 1 if hmac.compare_digest(ref, tag) else 0
    return ok >= t
