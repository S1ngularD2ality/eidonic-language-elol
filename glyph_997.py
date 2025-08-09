# glyph_997 – KEY_CONFUSION_DETECTOR
"""
Key-Context Confusion Detector

Detects accidental reuse of the same key across distinct contexts by keeping a
registry of (context -> key_hash). Raises on conflict.

APIs:
- class KeyRegistry().register(context: str, key: bytes) -> bool
"""

import hashlib

class KeyRegistry:
    def __init__(self):
        self.map = {}

    def register(self, context: str, key: bytes) -> bool:
        h = hashlib.blake2b(key, digest_size=16).hexdigest()
        if context in self.map:
            return self.map[context] == h
        # check if any other context uses identical key
        if h in self.map.values():
            return False
        self.map[context] = h
        return True
