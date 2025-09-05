def glyph_154(grid):
    """
    Returns a grid with each cell replaced by the sum of its coordinates.

    Example:
    Input: 2x2 grid
    Output: [[0,1],[1,2]]
    """
    return [[i + j for j in range(len(grid[0]))] for i in range(len(grid))]
