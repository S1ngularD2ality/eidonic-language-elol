# glyph_974 – HMAC_DRBG
"""
HMAC-DRBG (Deterministic Random Bit Generator)

RFC 6979-style generator using HMAC-BLAKE2b. Use to derive deterministic
nonces/keys from a seed and personalization.

APIs:
- class HmacDRBG(seed, personalization=b"")
  - reseed(additional_input)
  - random(n)->bytes
"""

import hmac, hashlib

class HmacDRBG:
    def __init__(self, seed: bytes, personalization: bytes = b""):
        self.K = b"\x00" * 64
        self.V = b"\x01" * 64
        self._update(seed + personalization)

    def _update(self, provided: bytes):
        self.K = hmac.new(self.K, self.V + b"\x00" + provided, hashlib.blake2b).digest()
        self.V = hmac.new(self.K, self.V, hashlib.blake2b).digest()
        if provided:
            self.K = hmac.new(self.K, self.V + b"\x01" + provided, hashlib.blake2b).digest()
            self.V = hmac.new(self.K, self.V, hashlib.blake2b).digest()

    def reseed(self, additional_input: bytes):
        self._update(additional_input)

    def random(self, n: int) -> bytes:
        out = b""
        while len(out) < n:
            self.V = hmac.new(self.K, self.V, hashlib.blake2b).digest()
            out += self.V
        return out[:n]
