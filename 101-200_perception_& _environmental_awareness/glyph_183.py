def glyph_183(n, m):
    """
    Creates a horizontal gradient from 0 to m-1.

    Example:
    Input: 3, 4
    Output: [[0,1,2,3],[0,1,2,3],[0,1,2,3]]
    """
    return [[j for j in range(m)] for _ in range(n)]
