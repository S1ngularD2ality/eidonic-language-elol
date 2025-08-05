def glyph_199(grid):
    """
    Sets adjacent cells to center value.

    Example:
    Input: [[0,0,0],[0,5,0],[0,0,0]]
    Output: [[0,5,0],[5,5,5],[0,5,0]]
    """
    from copy import deepcopy
    result = deepcopy(grid)
    n = len(grid)
    mid = n // 2
    val = grid[mid][mid]
    for i,j in [(mid-1,mid),(mid+1,mid),(mid,mid-1),(mid,mid+1)]:
        result[i][j] = val
    return result
