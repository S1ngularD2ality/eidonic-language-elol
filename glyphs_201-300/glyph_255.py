def glyph_255(n):
    """
    Glyph 255 — Shadow Map Constructor
    Constructs a matrix fading from edges to center.

    Example Input:
    3

    Output:
    [[2, 1, 2],
     [1, 0, 1],
     [2, 1, 2]]
    """
    return [[abs(i - n//2) + abs(j - n//2) for j in range(n)] for i in range(n)]
