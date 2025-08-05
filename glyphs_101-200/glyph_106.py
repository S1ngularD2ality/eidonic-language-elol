def glyph_106(matrix):
    """
    Encodes spiraling order from center outwards.
    """
    from math import ceil
    n = len(matrix)
    result = [[0]*n for _ in range(n)]
    layer = 0
    val = 1
    while layer < ceil(n / 2):
        for i in range(layer, n - layer): result[layer][i] = val; val += 1
        for i in range(layer + 1, n - layer): result[i][n - layer - 1] = val; val += 1
        for i in range(n - layer - 2, layer - 1, -1): result[n - layer - 1][i] = val; val += 1
        for i in range(n - layer - 2, layer, -1): result[i][layer] = val; val += 1
        layer += 1
    return result
