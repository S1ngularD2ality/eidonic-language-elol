def glyph_239(n):
    """
    Glyph 239 — Crystalline Perimeter Shell
    Creates an n x n grid with outer shell marked.

    Example Input:
    4

    Output:
    [[1, 1, 1, 1],
     [1, 0, 0, 1],
     [1, 0, 0, 1],
     [1, 1, 1, 1]]
    """
    return [[1 if i in (0, n-1) or j in (0, n-1) else 0 for j in range(n)] for i in range(n)]
