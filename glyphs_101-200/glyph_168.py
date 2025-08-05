def glyph_168(grid):
    """
    Doubles all values on the border of the grid.

    Example:
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[2,4,6],[4,5,6],[14,16,18]]
    """
    rows, cols = len(grid), len(grid[0])
    return [[
        val*2 if i==0 or j==0 or i==rows-1 or j==cols-1 else val
        for j, val in enumerate(row)
    ] for i, row in enumerate(grid)]
