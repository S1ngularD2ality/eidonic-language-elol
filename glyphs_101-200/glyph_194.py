def glyph_194(n):
    """
    Generates an n x n hollow square of 1s.

    Example:
    Input: 3
    Output: [[1,1,1],[1,0,1],[1,1,1]]
    """
    return [[1 if i in (0,n-1) or j in (0,n-1) else 0 for j in range(n)] for i in range(n)]
