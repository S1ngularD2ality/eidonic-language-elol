# glyph_965 – ROLLING_TAMPER_LOG
"""
Rolling Tamper-Evident Ring Buffer

Maintains a fixed-size ring of records; each slot stores (data, mac, prev_mac).
Any modification breaks downstream verification.

APIs:
- class RingLog(capacity:int, key:bytes)
  - append(data: bytes) -> index
  - verify() -> bool
"""

import hashlib, hmac
from typing import List, Tuple

class RingLog:
    def __init__(self, capacity: int, key: bytes):
        self.N = capacity
        self.key = key
        self.buf: List[Tuple[bytes, bytes, bytes]] = []  # (data, mac, prev)
        self.head = 0

    def _mac(self, data: bytes, prev: bytes) -> bytes:
        return hmac.new(self.key, prev + data, hashlib.blake2b).digest()

    def append(self, data: bytes) -> int:
        prev = self.buf[self.head-1][1] if self.buf else b"\x00"*64
        mac  = self._mac(data, prev)
        entry = (data, mac, prev)
        if len(self.buf) < self.N:
            self.buf.append(entry)
            self.head = len(self.buf)
        else:
            self.buf[self.head % self.N] = entry
            self.head = (self.head + 1) % self.N
        return (self.head - 1) % self.N

    def verify(self) -> bool:
        prev = b"\x00"*64
        for i in range(min(len(self.buf), self.N)):
            data, mac, p = self.buf[i]
            if p != prev: return False
            if self._mac(data, p) != mac: return False
            prev = mac
        return True
