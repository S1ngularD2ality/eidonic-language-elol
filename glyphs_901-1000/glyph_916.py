# glyph_916 – LATTICE_HARMONIC_SHUFFLER
"""
Lattice Harmonic Shuffler

PRNG-seeded block permutation keyed by a harmonic phrase. Deterministic mapping
for a given key; combine with block cipher or stream cipher upstream.
"""

import hashlib, random
from typing import List, Any

def lhs_permute(blocks: List[Any], phrase: bytes) -> List[Any]:
    seed = int.from_bytes(hashlib.sha3_512(phrase).digest()[:8], "big")
    rng = random.Random(seed)
    idx = list(range(len(blocks)))
    rng.shuffle(idx)
    return [blocks[i] for i in idx]
