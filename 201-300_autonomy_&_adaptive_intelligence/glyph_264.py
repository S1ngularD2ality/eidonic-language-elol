def glyph_264(n):
    """
    Glyph 264 — Radial Gate Sequencer
    Builds a gate of ascending outer layers.

    Example Input:
    3

    Output:
    [[1, 1, 1],
     [1, 2, 1],
     [1, 1, 1]]
    """
    return [[min(i, j, n-1-i, n-1-j)+1 for j in range(n)] for i in range(n)]
