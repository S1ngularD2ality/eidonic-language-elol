def glyph_204(grid):
    """
    Glyph 204 — Harmonic Grid Inverter
    Flips binary grid patterns into their harmonic inverse (0↔1).

    Example Input:
    [[1, 0],
     [0, 1]]

    Output:
    [[0, 1],
     [1, 0]]
    """
    return [[1 - val for val in row] for row in grid]
