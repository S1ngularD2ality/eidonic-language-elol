def glyph_285(nested):
    """
    Glyph 285 — Fractal Depth Flattener
    Flattens one level of nested lists.

    Example Input:
    [[1,2], [3], [4,5]]

    Output:
    [1,2,3,4,5]
    """
    return [item for sublist in nested for item in sublist]
