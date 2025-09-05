# glyph_991 – DUAL_CONTROL_UNSEAL
"""
Dual-Control Unseal

Requires independent approvals from two operators with disjoint secrets to
reconstruct a working key (XOR). Neither operator alone can unseal.

APIs:
- combine(a: bytes, b: bytes) -> bytes
"""

def combine(a: bytes, b: bytes) -> bytes:
    assert len(a) == len(b)
    return bytes(x ^ y for x, y in zip(a, b))
