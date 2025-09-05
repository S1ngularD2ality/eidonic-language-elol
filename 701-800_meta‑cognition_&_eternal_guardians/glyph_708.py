# glyph_708 – CODE_EVOLUTION_TRACK
# Cryptographically chain each change to form an immutable evolution log.

import hashlib
import time
from typing import Optional

class glyph_708:
    """
    .append(change) -> entry
    .chain_valid() -> bool
    """
    def __init__(self):
        self.chain = []  # each: {'ts','change','prev_hash','hash'}

    def _h(self, payload: str):
        return hashlib.sha256(payload.encode()).hexdigest()

    def append(self, change: str, ts: Optional[float] = None):
        ts = ts or time.time()
        prev_hash = self.chain[-1]["hash"] if self.chain else "0"*64
        payload = f"{ts}|{change}|{prev_hash}"
        h = self._h(payload)
        entry = {"ts": ts, "change": change, "prev_hash": prev_hash, "hash": h}
        self.chain.append(entry)
        return entry

    def chain_valid(self):
        prev = "0"*64
        for e in self.chain:
            payload = f"{e['ts']}|{e['change']}|{prev}"
            if self._h(payload) != e["hash"]:
                return False
            prev = e["hash"]
        return True
