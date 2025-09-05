def glyph_176(n):
    """
    Creates a grid where each row is shifted one step forward.

    Example:
    Input: 3
    Output: [[1,0,0],[0,1,0],[0,0,1]]
    """
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
