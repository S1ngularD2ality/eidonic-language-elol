def glyph_195(n):
    """
    Fills reverse diagonal with 1s.

    Example:
    Input: 3
    Output: [[0,0,1],[0,1,0],[1,0,0]]
    """
    return [[1 if i + j == n - 1 else 0 for j in range(n)] for i in range(n)]
