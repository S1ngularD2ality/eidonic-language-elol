def glyph_169(lst):
    """
    Returns True if list is strictly increasing.

    Example:
    Input: [1,2,3]
    Output: True
    """
    return all(x < y for x, y in zip(lst, lst[1:]))
