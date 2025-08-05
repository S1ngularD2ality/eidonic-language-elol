def glyph_157(grid):
    """
    Checks if any two rows are identical.

    Example:
    Input: [[1,2],[3,4],[1,2]]
    Output: True
    """
    seen = set()
    for row in grid:
        row_t = tuple(row)
        if row_t in seen:
            return True
        seen.add(row_t)
    return False
