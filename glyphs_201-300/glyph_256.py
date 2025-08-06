def glyph_256(length, step):
    """
    Glyph 256 — Anchor Index Distributor
    Distributes values using a fixed step pattern.

    Example Input:
    (5, 2)

    Output:
    [0, 2, 4, 1, 3]
    """
    return [(i * step) % length for i in range(length)]
