def glyph_178(grid):
    """
    Replaces all -1 with 0.

    Example:
    Input: [[1,-1],[2,-1]]
    Output: [[1,0],[2,0]]
    """
    return [[0 if val == -1 else val for val in row] for row in grid]
