def glyph_147(grid):
    """
    Reduces each row to its mean and returns a list of means.

    Example:
    Input: [[1, 2, 3], [4, 5, 6]]
    Output: [2.0, 5.0]
    """
    return [sum(row) / len(row) for row in grid]
