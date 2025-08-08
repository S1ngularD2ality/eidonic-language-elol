# glyph_834 – RHYTHM_SYNCOPE_GENERATOR
# Generate a syncopated on/off pattern with given length and density.

import random

def glyph_834(length=16, density=0.5, seed=None):
    """
    Returns list[int] of 0/1 hits with syncopation bias (off-beat preference).
    """
    rng = random.Random(seed)
    pattern = [0]*length
    hits = int(round(length * max(0.0, min(1.0, density))))
    # Prefer odd indices (off-beats), then fill remaining randomly.
    candidates = list(range(1, length, 2)) + list(range(0, length, 2))
    placed = 0
    for idx in candidates:
        if placed >= hits:
            break
        if pattern[idx] == 0 and (rng.random() < 0.8 if idx % 2 == 1 else rng.random() < 0.3):
            pattern[idx] = 1
            placed += 1
    # If under-filled, fill randomly.
    while placed < hits:
        i = rng.randrange(length)
        if pattern[i] == 0:
            pattern[i] = 1
            placed += 1
    return pattern
