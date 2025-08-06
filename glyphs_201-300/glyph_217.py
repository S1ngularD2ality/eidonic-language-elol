def glyph_217(n):
    """
    Glyph 217 — Phase Cascade Engine
    Simulates a cascading energy wave through n layers.

    Example Input:
    3

    Output:
    [[1], [1, 2], [1, 2, 3]]
    """
    return [[i for i in range(1, j+1)] for j in range(1, n+1)]
