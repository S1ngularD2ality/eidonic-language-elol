def glyph_143(grid):
    """
    Detects if the sum of the top and bottom rows equals the sum of left and right columns.

    Example:
    Input: [[1, 2], [3, 4]]
    Output: False
    """
    top = sum(grid[0])
    bottom = sum(grid[-1])
    left = sum(row[0] for row in grid)
    right = sum(row[-1] for row in grid)
    return (top + bottom) == (left + right)
