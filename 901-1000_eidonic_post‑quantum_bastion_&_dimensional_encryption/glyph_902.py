# glyph_902 – MIRROR_TETHERED_LOCK
"""
Mirror-Tethered Lock: opens only under coherence with an enrolled "reflection"
pattern (behavioral/harmonic vector) + challenge.

Flow:
- enroll(reference_vector) -> stores a salted digest.
- unlock(live_vector, challenge) compares against per-challenge digest.
"""

import os, hmac, hashlib

class MirrorTetheredLock:
    def __init__(self):
        self.salt = os.urandom(32)
        self.ref  = None

    def enroll(self, reference_vector: bytes):
        self.ref = hashlib.blake2b(reference_vector + self.salt, digest_size=64).digest()

    def derive(self, live_vector: bytes, challenge: bytes) -> bytes:
        return hashlib.blake2b(live_vector + self.salt + challenge, digest_size=64).digest()

    def unlock(self, live_vector: bytes, challenge: bytes) -> bool:
        assert self.ref is not None, "Not enrolled"
        return hmac.compare_digest(self.derive(live_vector, challenge), self.ref)
