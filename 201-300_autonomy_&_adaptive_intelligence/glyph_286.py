def glyph_286(a, b):
    """
    Glyph 286 — Temporal Thread Knotter
    Zips two lists and reverses pairs.

    Example Input:
    [1,2], [3,4]

    Output:
    [(3,1), (4,2)]
    """
    return [(y, x) for x, y in zip(a, b)]
