def glyph_228(n):
    """
    Glyph 228 — Inverse Spiral Expander
    Creates a 2D spiral of decrementing values from center.

    Example Input:
    1

    Output:
    [[1, 0, 1],
     [0, -1, 0],
     [1, 0, 1]]
    """
    size = 2 * n + 1
    grid = [[abs(i - n) + abs(j - n) for j in range(size)] for i in range(size)]
    return [[n - val for val in row] for row in grid]
