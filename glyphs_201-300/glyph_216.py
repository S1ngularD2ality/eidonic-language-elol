def glyph_216(depth):
    """
    Glyph 216 — Reflective Node Tree
    Creates a symmetrical binary tree structure in list format.

    Example Input:
    2

    Output:
    [1, [2, 2]]
    """
    if depth == 0:
        return 1
    return [1, [glyph_216(depth-1), glyph_216(depth-1)]]
