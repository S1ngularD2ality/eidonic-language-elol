# glyph_955 – DEVICE_BIND_ATTEST
"""
Device-Bind Attestation

Binds a session to a device-specific secret (e.g., TPM/TEE-held key).
Here we simulate with a per-device key and a nonce challenge.

APIs:
- attest(device_key, nonce) -> mac
- verify(device_pub_or_key, nonce, mac) -> bool
"""

import hmac, hashlib

def attest(device_key: bytes, nonce: bytes) -> bytes:
    return hmac.new(device_key, nonce, hashlib.blake2b).digest()

def verify(device_key: bytes, nonce: bytes, mac: bytes) -> bool:
    return hmac.compare_digest(attest(device_key, nonce), mac)
