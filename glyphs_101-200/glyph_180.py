def glyph_180(grid):
    """
    Multiplies all values by -1.

    Example:
    Input: [[1,-2],[3,0]]
    Output: [[-1,2],[-3,0]]
    """
    return [[-val for val in row] for row in grid]
