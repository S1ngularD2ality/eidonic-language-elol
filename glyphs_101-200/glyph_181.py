def glyph_181(grid):
    """
    Reflects the grid along its secondary diagonal.

    Example:
    Input: [[1,2],[3,4]]
    Output: [[4,3],[2,1]]
    """
    n = len(grid)
    return [[grid[n-j-1][n-i-1] for j in range(n)] for i in range(n)]
