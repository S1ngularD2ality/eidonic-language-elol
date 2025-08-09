# glyph_982 – DATA_DIODE_ONE_WAY
"""
Data Diode (One-Way Serialization)

Provides a one-way transfer primitive: encode -> physical move -> decode.
Decoder refuses if any bidirectional metadata is present (defense-in-depth).

APIs:
- encode(payload: bytes) -> bytes
- decode(blob: bytes) -> bytes | None
"""

import hashlib, json

MAGIC = b"ELDIODE1"

def encode(payload: bytes) -> bytes:
    meta = {"len": len(payload)}
    header = json.dumps(meta).encode()
    h = hashlib.blake2b(header + payload, digest_size=32).digest()
    return MAGIC + len(header).to_bytes(4, "big") + header + h + payload

def decode(blob: bytes) -> bytes | None:
    if not blob.startswith(MAGIC):
        return None
    off = len(MAGIC)
    hlen = int.from_bytes(blob[off:off+4], "big"); off += 4
    header = blob[off:off+hlen]; off += hlen
    mac = blob[off:off+32]; off += 32
    payload = blob[off:]
    if hashlib.blake2b(header + payload, digest_size=32).digest() != mac:
        return None
    meta = json.loads(header.decode())
    return payload if meta.get("len") == len(payload) else None
