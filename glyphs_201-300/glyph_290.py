def glyph_290(lst):
    """
    Glyph 290 — Phantom Index Tracker
    Returns list of (value, index) pairs.

    Example Input:
    [10, 20, 30]

    Output:
    [(10, 0), (20, 1), (30, 2)]
    """
    return list(zip(lst, range(len(lst))))
