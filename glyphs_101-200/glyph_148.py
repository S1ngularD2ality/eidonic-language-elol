def glyph_148(grid):
    """
    Extracts all non-zero values and returns their positions.

    Example:
    Input: [[0, 1], [2, 0]]
    Output: [(0,1), (1,0)]
    """
    return [(i, j) for i, row in enumerate(grid) for j, val in enumerate(row) if val != 0]
