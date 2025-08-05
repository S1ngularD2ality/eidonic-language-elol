def glyph_187(grid):
    """
    Counts number of zeros in center row and column.

    Example:
    Input: [[0,1,0],[2,0,3],[4,0,5]]
    Output: 4
    """
    n = len(grid)
    mid = n // 2
    row = grid[mid]
    col = [grid[i][mid] for i in range(n)]
    return row.count(0) + col.count(0) - (1 if grid[mid][mid] == 0 else 0)
