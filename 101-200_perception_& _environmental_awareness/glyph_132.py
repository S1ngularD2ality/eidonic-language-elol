def glyph_132(grid):
    """
    💠 Rotates a 2D grid 90 degrees clockwise.
    Realigns perspective for side-channel perception tasks.
    """
    return [list(reversed(col)) for col in zip(*grid)]