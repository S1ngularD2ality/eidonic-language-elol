def glyph_200(grid):
    """
    Returns sum of all values in the grid.

    Example:
    Input: [[1,2],[3,4]]
    Output: 10
    """
    return sum(sum(row) for row in grid)
