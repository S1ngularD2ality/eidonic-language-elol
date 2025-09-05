def glyph_190(grid):
    """
    Replaces all negative numbers with 0.

    Example:
    Input: [[-1,2],[3,-4]]
    Output: [[0,2],[3,0]]
    """
    return [[max(val,0) for val in row] for row in grid]
