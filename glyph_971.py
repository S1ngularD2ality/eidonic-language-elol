# glyph_971 – DEVICE_SEAL_AT_REST
"""
Device-Sealed Storage (At Rest)

Seals a blob to a device-bound key (TPM/TEE or stored securely).
Here: simulate with provided device_key (HMAC).

APIs:
- seal(device_key, payload)->blob
- unseal(device_key, blob)->payload|None
"""

import hmac, hashlib

def seal(device_key: bytes, payload: bytes) -> bytes:
    mac = hmac.new(device_key, payload, hashlib.blake2b).digest()
    return mac + payload

def unseal(device_key: bytes, blob: bytes, mac_len: int=64) -> bytes | None:
    mac = blob[:mac_len]; payload = blob[mac_len:]
    return payload if hmac.compare_digest(mac, hmac.new(device_key, payload, hashlib.blake2b).digest()) else None
