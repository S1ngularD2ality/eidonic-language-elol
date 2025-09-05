def glyph_223(matrix):
    """
    Glyph 223 — Dimensional Shift Counter
    Counts how many times each value appears in a 2D matrix.

    Example Input:
    [[1, 2, 2], [3, 1, 1]]

    Output:
    {1: 3, 2: 2, 3: 1}
    """
    from collections import Counter
    return dict(Counter([x for row in matrix for x in row]))
