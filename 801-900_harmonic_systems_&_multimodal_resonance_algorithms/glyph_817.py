# glyph_817 – CELESTIAL_ALIGNMENT_CALCULATOR
# Project timestamp into a 360° phase using φ.

PHI = (1 + 5 ** 0.5) / 2

def glyph_817(timestamp: float):
    """
    Returns phase in [0, 360) degrees.
    """
    return (timestamp * PHI) % 360.0
