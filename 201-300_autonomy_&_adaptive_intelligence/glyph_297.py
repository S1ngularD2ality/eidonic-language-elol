def glyph_297(lst, steps):
    """
    Glyph 297 — Orbital Pattern Shifter
    Rotates list left by steps.

    Example Input:
    [1,2,3,4], 1

    Output:
    [2,3,4,1]
    """
    return lst[steps:] + lst[:steps]
