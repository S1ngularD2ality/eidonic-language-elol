def glyph_262(n, mod):
    """
    Glyph 262 — Modular Sequence Sculptor
    Constructs a list of numbers modulated by given value.

    Example Input:
    (7, 3)

    Output:
    [0, 1, 2, 0, 1, 2, 0]
    """
    return [i % mod for i in range(n)]
