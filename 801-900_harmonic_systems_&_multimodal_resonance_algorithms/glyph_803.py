# glyph_803 – GOLDEN_RATIO_OPTIMIZER
# Move numeric values toward φ for stable harmonic balance.

PHI = (1 + 5 ** 0.5) / 2

def glyph_803(values):
    """
    values: iterable of numbers
    Returns list with each value nudged toward φ.
    """
    return [v + (PHI - v) * 0.5 for v in values]
