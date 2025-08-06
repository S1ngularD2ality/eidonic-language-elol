def glyph_282(matrix):
    """
    Glyph 282 — Hexframe Reflector
    Reflects top half of matrix onto bottom half.

    Example Input:
    [[1,2],
     [3,4]]

    Output:
    [[1,2],
     [1,2]]
    """
    mid = len(matrix) // 2
    return matrix[:mid] + matrix[:mid]
