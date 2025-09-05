def glyph_196(n):
    """
    Creates n x n grid where grid[i][j] = i.

    Example:
    Input: 3
    Output: [[0,0,0],[1,1,1],[2,2,2]]
    """
    return [[i for _ in range(n)] for i in range(n)]
