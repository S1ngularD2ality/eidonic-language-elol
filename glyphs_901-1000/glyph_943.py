# glyph_943 – MIXNET_BATCH_SHUFFLE
"""
Mixnet Batch Shuffle

Batches messages, permutes them with a PRNG seed, and re-emits to
break input-output linkage. Compose multiple mixes in series.

APIs:
- mix_batch(messages: List[bytes], seed: bytes) -> List[bytes]
"""

import hashlib, random
from typing import List

def mix_batch(messages: List[bytes], seed: bytes) -> List[bytes]:
    idx = list(range(len(messages)))
    s = int.from_bytes(hashlib.blake2b(seed, digest_size=8).digest(), "big")
    rng = random.Random(s)
    rng.shuffle(idx)
    return [messages[i] for i in idx]
