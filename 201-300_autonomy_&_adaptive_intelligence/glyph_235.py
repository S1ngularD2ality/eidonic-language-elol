def glyph_235(n):
    """
    Glyph 235 — Hex Grid Synthesizer
    Builds a symmetric hexagonal pattern using integers.

    Example Input:
    2

    Output:
    [[1],
     [1, 2],
     [1, 2, 3],
     [1, 2],
     [1]]
    """
    pattern = [[1 + j for j in range(i + 1)] for i in range(n)]
    return pattern + pattern[::-1][1:]
