def glyph_185(grid):
    """
    Zeros out everything except the center.

    Example:
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[0,0,0],[0,5,0],[0,0,0]]
    """
    n = len(grid)
    mid = n // 2
    return [[val if i==mid and j==mid else 0 for j, val in enumerate(row)] for i, row in enumerate(grid)]
