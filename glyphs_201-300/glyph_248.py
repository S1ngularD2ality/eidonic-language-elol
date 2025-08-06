def glyph_248(grid):
    """
    Glyph 248 — Recursive Grid Flipper
    Flips grid upside down and reverses rows.

    Example Input:
    [[1, 2],
     [3, 4]]

    Output:
    [[4, 3],
     [2, 1]]
    """
    return [row[::-1] for row in grid[::-1]]
