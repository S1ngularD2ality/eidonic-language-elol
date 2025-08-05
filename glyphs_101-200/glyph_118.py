def glyph_118(signal_map):
    """
    💠 Horizontally mirrors a 2D signal array.
    Used in bifurcation testing and twin-state reflection.
    """
    return [row[::-1] for row in signal_map]
