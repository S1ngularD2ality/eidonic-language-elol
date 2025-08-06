def glyph_288(a, b):
    """
    Glyph 288 — Dual State Comparator
    Returns element-wise comparison result.

    Example Input:
    [1,2,3], [3,2,1]

    Output:
    [False, True, False]
    """
    return [x == y for x, y in zip(a, b)]
