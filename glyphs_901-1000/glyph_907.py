# glyph_907 – PHASE_STATE_MIRROR_HASH
"""
Phase-State Mirror Hash

Hash that includes a caller-specified phase bucket, forcing attackers to match
phase context (time, rhythm, ritual step) in addition to payload.
"""

import hashlib

def phase_state_mirror_hash(data: bytes, phase_bucket: int) -> bytes:
    assert 0 <= phase_bucket < 360
    return hashlib.blake2b(data + phase_bucket.to_bytes(2, "big"), digest_size=64).digest()
