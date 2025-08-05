def glyph_184(n):
    """
    Generates an n x n checkerboard of 1s and 0s.

    Example:
    Input: 3
    Output: [[1,0,1],[0,1,0],[1,0,1]]
    """
    return [[(i+j)%2 for j in range(n)] for i in range(n)]
