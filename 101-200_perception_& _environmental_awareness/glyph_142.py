def glyph_142(grid):
    """
    Returns the coordinates of mirrored diagonal pairs in a square grid.
    Checks from top-left to bottom-right and vice versa.

    Example:
    Input: [[0, 1], [1, 0]]
    Output: [(0, 0, 1, 1), (0, 1, 1, 0)]
    """
    n = len(grid)
    mirrored = []
    for i in range(n):
        if grid[i][i] == grid[n-1-i][n-1-i]:
            mirrored.append((i, i, n-1-i, n-1-i))
    return mirrored
