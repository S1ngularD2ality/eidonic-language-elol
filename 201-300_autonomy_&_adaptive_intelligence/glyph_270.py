def glyph_270(arr):
    """
    Glyph 270 — Cascade Position Mapper
    Returns a dictionary mapping values to their indices.

    Example Input:
    [4, 2, 7]

    Output:
    {4: 0, 2: 1, 7: 2}
    """
    return {val: idx for idx, val in enumerate(arr)}
