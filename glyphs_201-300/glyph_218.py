def glyph_218(grid):
    """
    Glyph 218 — Polar Grid Inverter
    Converts a grid of positive/negative values into 1/0 based on polarity.

    Example Input:
    [[-1, 2], [0, -3]]

    Output:
    [[0, 1], [0, 0]]
    """
    return [[1 if x > 0 else 0 for x in row] for row in grid]
