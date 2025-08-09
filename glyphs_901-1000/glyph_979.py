# glyph_979 – SECURE_SNAPSHOT_CHECKPOINT
"""
Secure Snapshot Checkpoint

Creates incremental checkpoints of state with chained MACs; supports rollback
detection and quick verification.

APIs:
- class Checkpointer(key).checkpoint(state_bytes)->record; verify(stream)->bool
"""

import hashlib, hmac, json
from typing import List

class Checkpointer:
    def __init__(self, key: bytes):
        self.key = key
        self.prev = b"\x00"*32
        self.stream: List[bytes] = []

    def checkpoint(self, state: bytes) -> bytes:
        mac = hmac.new(self.key, self.prev + state, hashlib.blake2b).digest()
        rec = json.dumps({"prev": self.prev.hex(), "mac": mac.hex(), "state": state.hex()}).encode()
        self.prev = mac
        self.stream.append(rec)
        return rec

    def verify(self, stream: List[bytes] | None = None) -> bool:
        prev = b"\x00"*32
        for r in (stream or self.stream):
            obj = json.loads(r.decode())
            state = bytes.fromhex(obj["state"]); mac = bytes.fromhex(obj["mac"])
            if not hmac.compare_digest(hmac.new(self.key, prev + state, hashlib.blake2b).digest(), mac):
                return False
            prev = mac
        return True
