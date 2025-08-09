# glyph_967 – REMOTE_ATTEST_NONCE
"""
Remote Attestation (Nonce + Claims MAC)

Proves a device/service is in a declared state for a given nonce.
The verifier checks MAC(key, nonce || claims). Claims can include
versions, hashes, and configuration.

APIs:
- attest(key, nonce, claims)->tag
- verify(key, nonce, claims, tag)->bool
"""

import hmac, hashlib

def attest(key: bytes, nonce: bytes, claims: bytes) -> bytes:
    return hmac.new(key, nonce + claims, hashlib.blake2b).digest()

def verify(key: bytes, nonce: bytes, claims: bytes, tag: bytes) -> bool:
    return hmac.compare_digest(attest(key, nonce, claims), tag)
