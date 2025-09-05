def glyph_166(grid):
    """
    Calculates the difference between max and min values in the grid.

    Example:
    Input: [[3,5,7],[1,2,9]]
    Output: 9 - 1 = 8
    """
    flat = [val for row in grid for val in row]
    return max(flat) - min(flat)
