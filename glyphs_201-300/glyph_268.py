def glyph_268(a, b, c):
    """
    Glyph 268 — Tri-Thread Combiner
    Combines three arrays in alternating order.

    Example Input:
    [1], [2], [3]

    Output:
    [1, 2, 3]
    """
    return [val for triple in zip(a, b, c) for val in triple]
