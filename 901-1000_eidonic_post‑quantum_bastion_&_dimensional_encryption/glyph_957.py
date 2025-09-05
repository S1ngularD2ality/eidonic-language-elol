# glyph_957 – KEY_ERASURE_TIMER
"""
Key Erasure Timer

Holds a key in a closure and destroys it after timeout or explicit revoke.
Access after destruction returns None.

APIs:
- KeyTimer(key: bytes, ttl_s: float).get()->bytes|None, .revoke()->None
"""

import time

class KeyTimer:
    def __init__(self, key: bytes, ttl_s: float):
        self._key = bytearray(key)
        self.exp = time.time() + ttl_s
        self.dead = False

    def get(self):
        if self.dead or time.time() > self.exp:
            self.revoke()
            return None
        return bytes(self._key)

    def revoke(self):
        for i in range(len(self._key)):
            self._key[i] = 0
        self.dead = True
