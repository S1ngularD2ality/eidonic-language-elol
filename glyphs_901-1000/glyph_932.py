# glyph_932 – ATTESTATION_ENVELOPE
"""
Attestation Envelope

Wrap payload with integrity + environment attestation (claims).
- claims: b64/json externally; here opaque bytes.
- Produces envelope: HMAC(claims||payload) || claims || payload

APIs:
- seal(payload, claims, key) -> bytes
- open_and_verify(envelope, key) -> (claims, payload) or None
"""

import hashlib, hmac

def seal(payload: bytes, claims: bytes, key: bytes) -> bytes:
    mac = hmac.new(key, claims + payload, hashlib.blake2b).digest()
    return mac + claims + payload

def open_and_verify(envelope: bytes, key: bytes, mac_len: int = 64) -> tuple | None:
    mac = envelope[:mac_len]
    rest = envelope[mac_len:]
    # Without length tags, caller must know claims split; demo assumes half
    mid = len(rest)//2
    claims, payload = rest[:mid], rest[mid:]
    if hmac.compare_digest(mac, hmac.new(key, claims + payload, hashlib.blake2b).digest()):
        return claims, payload
    return None
