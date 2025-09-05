def glyph_160(n):
    """
    Generates a square matrix where values increase radially outward from the center.

    Example:
    Input: 3
    Output: [[2,1,2],[1,0,1],[2,1,2]]
    """
    center = n // 2
    return [[abs(i - center) + abs(j - center) for j in range(n)] for i in range(n)]
