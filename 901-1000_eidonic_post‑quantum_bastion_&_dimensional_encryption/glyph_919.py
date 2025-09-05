# glyph_919 – ENTROPY_HARVEST_LOCK
"""
Entropy Harvest Lock

Generates keys from OS CSPRNG augmented by timing jitter measurement.
Returns (key, attestation) where attestation binds a tiny jitter record.
"""

import os, time, hashlib
from typing import Tuple

def ehl_key(length: int = 32, jitter_samples: int = 64) -> Tuple[bytes, bytes]:
    jitter = []
    last = time.perf_counter_ns()
    for _ in range(jitter_samples):
        for _ in range(1000):
            pass
        now = time.perf_counter_ns()
        jitter.append(now - last); last = now
    jitter_bytes = b"".join(int(x).to_bytes(8, "little", signed=False) for x in jitter)
    seed = hashlib.sha3_512(os.urandom(64) + jitter_bytes).digest()
    key  = hashlib.blake2b(seed, digest_size=length).digest()
    attest = hashlib.blake2b(jitter_bytes, digest_size=32).digest()
    return key, attest
