def glyph_189(grid):
    """
    Collapses columns into row sums.

    Example:
    Input: [[1,2,3],[4,5,6]]
    Output: [5,7,9]
    """
    return [sum(col) for col in zip(*grid)]
