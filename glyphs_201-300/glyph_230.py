def glyph_230(values):
    """
    Glyph 230 — Linear Mirror Sweep
    Reflects the input list over its midpoint.

    Example Input:
    [1, 2, 3]

    Output:
    [1, 2, 3, 2, 1]
    """
    return values + values[-2::-1]
