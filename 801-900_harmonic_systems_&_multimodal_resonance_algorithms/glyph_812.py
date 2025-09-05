# glyph_812 – INFINITE_SPIRAL_PREDICTOR
# Log-spiral extrapolation using φ progression.

PHI = (1 + 5 ** 0.5) / 2

def glyph_812(seed: float, steps: int = 5):
    """
    Returns a list: seed * φ^i for i in [0..steps-1]
    """
    return [seed * (PHI ** i) for i in range(max(0, steps))]
