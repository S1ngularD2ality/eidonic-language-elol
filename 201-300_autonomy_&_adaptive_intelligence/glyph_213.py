def glyph_213(a, b):
    """
    Glyph 213 — Interlace Depth Matrix
    Interlaces two matrices row by row into a single depth field.

    Example Input:
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]

    Output:
    [[1, 2], [5, 6], [3, 4], [7, 8]]
    """
    result = []
    for i in range(len(a)):
        result.append(a[i])
        result.append(b[i])
    return result
