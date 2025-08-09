# glyph_946 – CHAFF_AND_WINNOW
"""
Chaffing & Winnowing (Message Authentication without Explicit Encryption)

Sender splits a message into packets, authenticates each with MAC using a shared
secret, and injects 'chaff' packets with invalid MACs. Receiver 'winnows' wheat
from chaff using MAC verification.

APIs:
- winnow(packets: List[tuple(payload, mac)], key: bytes) -> bytes (reassembled)
- mac(payload, key) -> bytes
"""

import hmac, hashlib
from typing import List, Tuple

def mac(payload: bytes, key: bytes) -> bytes:
    return hmac.new(key, payload, hashlib.blake2b).digest()

def winnow(packets: List[Tuple[bytes, bytes]], key: bytes) -> bytes:
    valid = [p for p, m in packets if hmac.compare_digest(mac(p, key), m)]
    return b"".join(valid)
