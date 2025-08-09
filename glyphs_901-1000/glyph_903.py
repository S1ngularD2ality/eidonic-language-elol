# glyph_903 – DIMENSIONAL_SHARD_ENCODER
"""
Dimensional Shard Encoder (All-or-N XOR Secret Split)

Splits data into N shards so that ALL shards are required to reconstruct.
Each shard is a random pad except the final which xors to the original.

Use when k=n threshold is acceptable and you prefer stream simplicity.
For k-of-n, compose with Shamir's Secret Sharing externally.
"""

import os
from typing import List

def shard_encode_all_or_n(data: bytes, n: int) -> List[bytes]:
    assert n >= 2
    pads = [os.urandom(len(data)) for _ in range(n-1)]
    x = bytes([b for b in data])
    for p in pads: x = bytes(a ^ b for a, b in zip(x, p))
    return pads + [x]

def shard_decode_all_or_n(shards: List[bytes]) -> bytes:
    assert len(shards) >= 2
    out = bytes([0]*len(shards[0]))
    for s in shards:
        assert len(s) == len(out)
        out = bytes(a ^ b for a, b in zip(out, s))
    return out
