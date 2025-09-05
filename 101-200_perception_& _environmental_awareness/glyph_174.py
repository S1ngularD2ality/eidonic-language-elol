def glyph_174(grid):
    """
    Reverses every row of the grid.

    Example:
    Input: [[1,2],[3,4]]
    Output: [[2,1],[4,3]]
    """
    return [row[::-1] for row in grid]
