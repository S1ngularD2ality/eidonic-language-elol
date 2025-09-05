# glyph_917 – FRACTAL_KEY_VAULT
"""
Fractal Key Vault

Recursive hash ladder storing derived keys across depths. Retrieval checks a
path-of-hashes; tampering changes the entire spine.
"""

import hashlib
from typing import List

def fkv_build(root_key: bytes, depth: int) -> List[bytes]:
    spine = [root_key]
    for _ in range(depth):
        spine.append(hashlib.blake2b(spine[-1], digest_size=32).digest())
    return spine

def fkv_verify(spine: List[bytes]) -> bool:
    for i in range(1, len(spine)):
        if hashlib.blake2b(spine[i-1], digest_size=32).digest() != spine[i]:
            return False
    return True
