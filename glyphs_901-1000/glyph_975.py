# glyph_975 – LOG_STRUCTURED_STORAGE_SEAL
"""
Log-Structured Storage Seal

Appends records with per-record MAC and a root commitment over the entire log.
Supports verifying integrity without decrypting contents.

APIs:
- class LSS(key).append(data)->rec; root()->bytes; verify(stream)->bool
"""

import hashlib, hmac, json
from typing import List

class LSS:
    def __init__(self, key: bytes):
        self.key = key
        self.recs: List[bytes] = []

    def append(self, data: bytes) -> bytes:
        mac = hmac.new(self.key, data, hashlib.blake2b).digest()
        rec = json.dumps({"d": data.hex(), "m": mac.hex()}).encode()
        self.recs.append(rec)
        return rec

    def root(self) -> bytes:
        h = hashlib.blake2b(digest_size=32)
        for r in self.recs:
            h.update(r)
        return h.digest()

    def stream(self) -> List[bytes]:
        return list(self.recs)

def verify(key: bytes, stream: List[bytes]) -> bool:
    for r in stream:
        obj = json.loads(r.decode())
        d = bytes.fromhex(obj["d"]); m = bytes.fromhex(obj["m"])
        if not hmac.compare_digest(hmac.new(key, d, hashlib.blake2b).digest(), m):
            return False
    return True
