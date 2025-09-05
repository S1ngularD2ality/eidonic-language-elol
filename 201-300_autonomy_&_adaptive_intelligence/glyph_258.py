def glyph_258(arr, threshold):
    """
    Glyph 258 — Threshold Echo Cutter
    Removes values below threshold, keeps order.

    Example Input:
    ([1, 3, 7, 2], 3)

    Output:
    [3, 7]
    """
    return [x for x in arr if x >= threshold]
