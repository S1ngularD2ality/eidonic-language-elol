def glyph_271(lst):
    """
    Glyph 271 — Temporal Pivot Cycler
    Moves center of list to front, preserving order.

    Example Input:
    [1, 2, 3, 4, 5]

    Output:
    [3, 4, 5, 1, 2]
    """
    mid = len(lst) // 2
    return lst[mid:] + lst[:mid]
