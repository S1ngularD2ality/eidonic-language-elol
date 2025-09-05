def glyph_284(lst):
    """
    Glyph 284 — Syntropic Reverser
    Reverses elements if they are increasing.

    Example Input:
    [1, 2, 3]

    Output:
    [3, 2, 1]
    """
    return lst[::-1] if lst == sorted(lst) else lst
