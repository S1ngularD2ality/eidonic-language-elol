def glyph_289(s):
    """
    Glyph 289 — Mirror Braid Generator
    Returns list of character pairs and their mirror.

    Example Input:
    'abc'

    Output:
    [('a','c'), ('b','b'), ('c','a')]
    """
    return list(zip(s, s[::-1]))
