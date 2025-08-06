def glyph_266(arr, mod):
    """
    Glyph 266 — Pulse Mod Thresholder
    Filters array based on value % mod == 0.

    Example Input:
    ([2, 4, 7, 9], 2)

    Output:
    [2, 4]
    """
    return [x for x in arr if x % mod == 0]
