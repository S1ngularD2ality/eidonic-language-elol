# glyph_918 – MULTIMODAL_AUTH_MESH
"""
Multimodal Auth Mesh

Fuses multiple modality hashes (voice/gesture/text/face/etc.) into one
attestation digest. Supports weighted fusion to prioritize certain modalities.
"""

import hashlib
from typing import List, Tuple

def mam_fuse(modality_hashes: List[bytes], weights: List[float] = None) -> bytes:
    if not modality_hashes:
        return b""
    if weights is None:
        weights = [1.0]*len(modality_hashes)
    assert len(weights) == len(modality_hashes)
    acc = b""
    for h, w in zip(modality_hashes, weights):
        wbytes = int(w * 1e6).to_bytes(8, "big", signed=True)
        acc += hashlib.blake2b(h + wbytes, digest_size=32).digest()
    return hashlib.blake2b(acc, digest_size=64).digest()
