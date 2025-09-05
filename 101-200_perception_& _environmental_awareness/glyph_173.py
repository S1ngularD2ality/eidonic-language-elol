def glyph_173(grid):
    """
    Returns True if there exists a row of only zeros.

    Example:
    Input: [[1,0],[0,0]]
    Output: True
    """
    return any(all(cell == 0 for cell in row) for row in grid)
