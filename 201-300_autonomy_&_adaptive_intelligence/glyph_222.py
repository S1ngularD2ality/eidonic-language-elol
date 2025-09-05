def glyph_222(n):
    """
    Glyph 222 — Nested Horizon Map
    Creates concentric numeric layers in a grid.

    Example Input:
    2

    Output:
    [[2, 2, 2],
     [2, 1, 2],
     [2, 2, 2]]
    """
    size = 2 * n + 1
    grid = [[n for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            grid[i][j] -= min(i, j, size - 1 - i, size - 1 - j)
    return grid
