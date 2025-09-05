def glyph_226(levels):
    """
    Glyph 226 — Pulse Layer Compiler
    Constructs layered pulse grids from integer levels.

    Example Input:
    3

    Output:
    [[1], [1, 1], [1, 1, 1]]
    """
    return [[1]*i for i in range(1, levels+1)]
