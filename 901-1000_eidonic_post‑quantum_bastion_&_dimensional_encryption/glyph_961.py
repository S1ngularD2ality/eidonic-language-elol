# glyph_961 – SECURE_BOOT_ANCHOR
"""
Secure Boot Anchor (Measured Boot Chain)

Computes a chained measurement over boot stages or modules to detect tampering.
Each stage extends the chain with H(stage || previous_digest). Store the final
anchor in a TPM/TEE or remote notary.

APIs:
- class BootChain: extend(blob: bytes) -> None; anchor() -> bytes
- verify(modules: List[bytes], expected_anchor: bytes) -> bool
"""

import hashlib
from typing import List

def _H(x: bytes) -> bytes:
    return hashlib.blake2b(x, digest_size=32).digest()

class BootChain:
    def __init__(self):
        self._d = b"\x00" * 32

    def extend(self, stage_blob: bytes) -> None:
        self._d = _H(stage_blob + self._d)

    def anchor(self) -> bytes:
        return self._d

def verify(modules: List[bytes], expected_anchor: bytes) -> bool:
    bc = BootChain()
    for m in modules:
        bc.extend(m)
    return bc.anchor() == expected_anchor
