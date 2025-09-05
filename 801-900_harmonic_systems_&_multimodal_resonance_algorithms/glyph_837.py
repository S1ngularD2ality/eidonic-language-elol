# glyph_837 – POLYHEDRAL_DICE_ROLLER
# Roll common polyhedral dice with optional seed (d4,d6,d8,d10,d12,d20).

import random

def glyph_837(sides=20, rolls=1, seed=None):
    """
    Returns list of rolls in [1..sides].
    """
    if sides < 2 or rolls < 1:
        raise ValueError("sides>=2, rolls>=1")
    rng = random.Random(seed)
    return [rng.randint(1, sides) for _ in range(rolls)]
