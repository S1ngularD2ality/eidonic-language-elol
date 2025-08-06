def glyph_293(a, b):
    """
    Glyph 293 — Binary Weave Lens
    Alternates characters from two strings.

    Example Input:
    "ab", "12"

    Output:
    "a1b2"
    """
    return ''.join(i + j for i, j in zip(a, b))
