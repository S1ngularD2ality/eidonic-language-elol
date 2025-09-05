def glyph_179(grid):
    """
    Returns the outer ring of a grid as a flat list.

    Example:
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,2,3,6,9,8,7,4]
    """
    top = grid[0]
    right = [row[-1] for row in grid[1:-1]]
    bottom = grid[-1][::-1]
    left = [row[0] for row in grid[-2:0:-1]]
    return top + right + bottom + left
