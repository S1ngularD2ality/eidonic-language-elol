def glyph_161(grid):
    """
    Returns True if the grid is horizontally symmetrical.

    Example:
    Input: [[1,2,1],[3,4,3]]
    Output: True
    """
    return all(row == row[::-1] for row in grid)
