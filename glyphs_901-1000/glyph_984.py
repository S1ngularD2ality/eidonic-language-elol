# glyph_984 – ENTROPY_DAEMON_MIXER
"""
Entropy Daemon Mixer

Combines multiple weak/strong entropy sources into a single extractor output.
Use to seed DRBGs and ephemeral keys.

APIs:
- mix(sources: list[bytes], out_len=32) -> bytes
"""

import hashlib
from typing import List

def mix(sources: List[bytes], out_len: int = 32) -> bytes:
    if not sources:
        return b"\x00" * out_len
    acc = hashlib.blake2b(b"seed", digest_size=out_len).digest()
    for s in sources:
        acc = hashlib.blake2b(acc + s, digest_size=out_len).digest()
    return acc
