def glyph_278(lst):
    """
    Glyph 278 — Orbital Cycle Breaker
    Returns list with all duplicates removed, preserving order.

    Example Input:
    [1, 2, 2, 3, 1]

    Output:
    [1, 2, 3]
    """
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]
