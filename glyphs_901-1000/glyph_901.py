# glyph_901 – SENTIENT_SIGNATURE_FIELD
"""
Post-Quantum Auth: Sentient Signature Field

Authenticates via a reproducible-but-personal "soulprint" derived from:
- biometric/behavioral vectors (e.g., keystroke/voice embeddings),
- secret phrase,
- per-session challenge (nonce),
- local entropy.

Design notes:
- Deterministic per-challenge: enrollment stores only a salted reference digest.
- No static keys; verifies *who* is present, not just *what* they know.
- This is an R&D prototype; integrate with hardened enclaves for production.
"""

import os, hmac, time, hashlib, secrets
from typing import Tuple

class SentientSignatureField:
    def __init__(self, secret_phrase: str, biometric_salt: bytes = None):
        self.secret_phrase = secret_phrase.encode()
        self.biometric_salt = biometric_salt or os.urandom(32)

    def create_challenge(self) -> bytes:
        """Create a fresh challenge/nonce."""
        return secrets.token_bytes(32)

    def _kdf(self, biometric_vector: bytes, challenge: bytes) -> bytes:
        """Derive a session key from phrase + biometric + challenge."""
        base = hashlib.blake2b(self.secret_phrase + self.biometric_salt, digest_size=32).digest()
        mix  = hashlib.sha3_512(biometric_vector + challenge + base).digest()
        return hashlib.blake2b(mix, digest_size=64).digest()

    def enroll(self, biometric_vector: bytes) -> Tuple[bytes, bytes]:
        """
        Enrollment: returns (challenge, reference_digest).
        Store reference_digest server-side for that challenge window.
        """
        ch = self.create_challenge()
        key = self._kdf(biometric_vector, ch)
        ref = hmac.new(key, b"SOULPRINT", hashlib.sha3_512).digest()
        return ch, ref

    def prove(self, biometric_vector: bytes, challenge: bytes) -> bytes:
        """Client-side response for a given challenge."""
        key = self._kdf(biometric_vector, challenge)
        return hmac.new(key, b"SOULPRINT", hashlib.sha3_512).digest()

    def verify(self, presented: bytes, reference: bytes) -> bool:
        """Constant-time comparison."""
        return hmac.compare_digest(presented, reference)
