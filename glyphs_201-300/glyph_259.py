def glyph_259(n):
    """
    Glyph 259 — Radiant Expansion Loop
    Builds a growing + shrinking loop pattern.

    Example Input:
    4

    Output:
    [1, 2, 3, 4, 3, 2, 1]
    """
    return list(range(1, n+1)) + list(range(n-1, 0, -1))
