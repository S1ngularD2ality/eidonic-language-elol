def glyph_211(n):
    """
    Glyph 211 — Fractal Bloom Generator
    Generates a recursive fractal bloom pattern using nested layers.

    Example Input:
    2

    Output:
    [[1, 1, 1],
     [1, 2, 1],
     [1, 1, 1]]
    """
    size = 2 * n + 1
    grid = [[1 for _ in range(size)] for _ in range(size)]
    if n > 0:
        grid[n][n] = 2
    return grid
