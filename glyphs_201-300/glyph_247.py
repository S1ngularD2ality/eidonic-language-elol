def glyph_247(n):
    """
    Glyph 247 — Nested Layer Invoker
    Fills matrix with concentric layers of descending values.

    Example Input:
    3

    Output:
    [[3, 3, 3],
     [3, 2, 3],
     [3, 3, 3]]
    """
    matrix = [[0]*n for _ in range(n)]
    for layer in range((n+1)//2):
        val = n - layer
        for i in range(layer, n-layer):
            for j in range(layer, n-layer):
                matrix[i][j] = val
    return matrix
