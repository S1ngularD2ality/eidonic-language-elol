def glyph_269(n):
    """
    Glyph 269 — Harmonic Reflection Line
    Builds a line that reflects in harmonic decreasing order.

    Example Input:
    4

    Output:
    [1, 2, 2, 1]
    """
    return list(range(1, n//2+1)) + list(range(n//2, 0, -1))
