def glyph_240(grid):
    """
    Glyph 240 — Singularity Center Scanner
    Returns the central element of an odd-sized 2D grid.

    Example Input:
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

    Output:
    5
    """
    n = len(grid)
    return grid[n//2][n//2]
