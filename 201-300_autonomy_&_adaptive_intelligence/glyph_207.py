def glyph_207(n):
    """
    Glyph 207 — Recursive Echo Core
    Produces a recursive echo pattern from the center outward.

    Example Input:
    3

    Output:
    [3, 2, 1, 1, 2, 3]
    """
    return list(range(n, 0, -1)) + list(range(1, n+1))
