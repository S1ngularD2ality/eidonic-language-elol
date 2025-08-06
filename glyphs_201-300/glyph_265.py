def glyph_265(arr):
    """
    Glyph 265 — Mirror Position Isolator
    Returns index pairs of mirrored values.

    Example Input:
    [2, 3, 2, 4]

    Output:
    [(0, 2)]
    """
    return [(i, j) for i in range(len(arr)) for j in range(i+1, len(arr)) if arr[i] == arr[j]]
