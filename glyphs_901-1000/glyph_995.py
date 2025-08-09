# glyph_995 – PACKET_HMAC_SEALER
"""
Packet HMAC Sealer

Seals packets with sequence-bound HMAC to prevent reordering/replay.

APIs:
- seal(pkt: bytes, seq: int, key: bytes) -> bytes  (mac||seq||pkt)
- open(blob: bytes, key: bytes) -> (seq, pkt)|None
"""

import hmac, hashlib

def seal(pkt: bytes, seq: int, key: bytes) -> bytes:
    seq_b = seq.to_bytes(8, "big")
    mac = hmac.new(key, seq_b + pkt, hashlib.blake2b).digest()
    return mac + seq_b + pkt

def open(blob: bytes, key: bytes) -> tuple[int, bytes] | None:
    mac = blob[:64]; seq_b = blob[64:72]; pkt = blob[72:]
    if hmac.compare_digest(mac, hmac.new(key, seq_b + pkt, hashlib.blake2b).digest()):
        return int.from_bytes(seq_b, "big"), pkt
    return None
