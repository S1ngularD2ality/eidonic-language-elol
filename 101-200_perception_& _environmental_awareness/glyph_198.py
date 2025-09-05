def glyph_198(grid):
    """
    Mirrors the top half vertically onto the bottom.

    Example:
    Input: [[1,2],[3,4]]
    Output: [[1,2],[1,2]]
    """
    mid = len(grid) // 2
    return grid[:mid] + grid[:mid]
