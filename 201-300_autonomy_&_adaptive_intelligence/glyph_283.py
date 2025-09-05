def glyph_283(n):
    """
    Glyph 283 — Scalar Vortex Divider
    Returns list of integers dividing n evenly.

    Example Input:
    6

    Output:
    [1, 2, 3, 6]
    """
    return [i for i in range(1, n+1) if n % i == 0]
