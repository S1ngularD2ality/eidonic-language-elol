# glyph_906 – INTENTION_LOCK
"""
Intention Lock

Binds access to a declared Purpose string. The verifier derives a digest from
Purpose + salt; clients must reproduce the same digest via PBKDF2 on their
intent token. Use distinct salts per lock.
"""

import os, hashlib, hmac

class IntentionLock:
    def __init__(self, purpose: str):
        self.salt = os.urandom(16)
        self.ref  = hashlib.pbkdf2_hmac("sha256", purpose.encode(), self.salt, 200_000, 32)

    def verify(self, presented_intent: str) -> bool:
        test = hashlib.pbkdf2_hmac("sha256", presented_intent.encode(), self.salt, 200_000, 32)
        return hmac.compare_digest(test, self.ref)
