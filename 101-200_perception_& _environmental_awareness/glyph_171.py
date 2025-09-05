def glyph_171(grid):
    """
    Replaces the center row and column with '*'.

    Example:
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,'*',3],['*','*','*'],[7,'*',9]]
    """
    n = len(grid)
    mid = n // 2
    return [
        ['*' if i == mid or j == mid else val for j, val in enumerate(row)]
        for i, row in enumerate(grid)
    ]
