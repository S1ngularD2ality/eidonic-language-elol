def glyph_191(grid):
    """
    Sets all border values of the grid to 9.

    Example:
    Input: [[0,0,0],[0,0,0],[0,0,0]]
    Output: [[9,9,9],[9,0,9],[9,9,9]]
    """
    n = len(grid)
    m = len(grid[0])
    return [[9 if i==0 or j==0 or i==n-1 or j==m-1 else grid[i][j] for j in range(m)] for i in range(n)]
