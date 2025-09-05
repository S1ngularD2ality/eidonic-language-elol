def glyph_244(grid):
    """
    Glyph 244 — Harmonic Line Equalizer
    Replaces each row with the average of its elements.

    Example Input:
    [[2, 4],
     [6, 8]]

    Output:
    [[3, 3],
     [7, 7]]
    """
    return [[sum(row) // len(row)] * len(row) for row in grid]
