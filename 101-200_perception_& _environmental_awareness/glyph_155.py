def glyph_155(seq):
    """
    Reverses a list and inverts boolean-like values (1 to 0, 0 to 1).

    Example:
    Input: [0,1,1]
    Output: [0,0,1]
    """
    return [1 - x for x in reversed(seq)]
