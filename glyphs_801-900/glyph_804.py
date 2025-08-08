# glyph_804 – MERKABA_STATE_SYNCHRONIZER
# Dual-tetrahedral balance function for two state phases.

import math

def glyph_804(state_a: float, state_b: float):
    """
    Returns a balanced scalar in [-1, 1] from sine/cosine coupling.
    """
    return (math.sin(state_a) + math.cos(state_b)) / 2.0
