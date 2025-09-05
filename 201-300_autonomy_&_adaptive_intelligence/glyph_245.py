def glyph_245(n):
    """
    Glyph 245 — Mirror Frame Invoker
    Creates an n x n frame with ones on edges and zeros inside.

    Example Input:
    3

    Output:
    [[1, 1, 1],
     [1, 0, 1],
     [1, 1, 1]]
    """
    return [[1 if i in (0, n-1) or j in (0, n-1) else 0 for j in range(n)] for i in range(n)]
