def glyph_151(grid):
    """
    Returns all elements from the main diagonal and anti-diagonal of a square grid.

    Example:
    Input: [[1,2,3],[4,5,6],[7,8,9]]
    Output: [1,5,9,3,5,7]
    """
    n = len(grid)
    main_diag = [grid[i][i] for i in range(n)]
    anti_diag = [grid[i][n - i - 1] for i in range(n)]
    return main_diag + anti_diag
