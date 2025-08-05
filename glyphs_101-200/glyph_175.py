def glyph_175(grid):
    """
    Transposes the grid (swaps rows with columns).

    Example:
    Input: [[1,2],[3,4]]
    Output: [[1,3],[2,4]]
    """
    return [list(col) for col in zip(*grid)]
