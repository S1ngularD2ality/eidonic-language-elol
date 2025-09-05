# glyph_939 – RANDOMNESS_EXTRACTOR
"""
Multi-Source Randomness Extractor

XOR mixer + hash extractor over multiple entropy sources.
Use to combine OS CSPRNG with hardware noise/jitter channels.

APIs:
- extract(sources: List[bytes], out_len=32) -> bytes
"""

import hashlib
from typing import List

def extract(sources: List[bytes], out_len: int = 32) -> bytes:
    if not sources: return b"\x00"*out_len
    mix = sources[0]
    for s in sources[1:]:
        L = min(len(mix), len(s))
        mix = bytes(a ^ b for a, b in zip(mix[:L], s[:L]))
    return hashlib.blake2b(mix, digest_size=out_len).digest()
