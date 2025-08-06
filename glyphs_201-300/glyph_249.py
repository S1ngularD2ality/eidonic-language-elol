def glyph_249(arr):
    """
    Glyph 249 — Echo Collapse Sorter
    Removes duplicates, then sorts the result.

    Example Input:
    [5, 3, 2, 5, 3, 1]

    Output:
    [1, 2, 3, 5]
    """
    return sorted(set(arr))
