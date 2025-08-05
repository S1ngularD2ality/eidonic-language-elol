def glyph_163(grid):
    """
    Sums the values of all diagonals from top-left to bottom-right.

    Example:
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: 1+5+9 = 15
    """
    return sum(grid[i][i] for i in range(min(len(grid), len(grid[0]))))
