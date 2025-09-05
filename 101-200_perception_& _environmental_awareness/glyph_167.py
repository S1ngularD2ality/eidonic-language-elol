def glyph_167(grid):
    """
    Returns a list of booleans indicating if each column is uniform.

    Example:
    Input: [[1,2],[1,2],[1,3]]
    Output: [True, False]
    """
    return [len(set(row[i] for row in grid)) == 1 for i in range(len(grid[0]))]
