def glyph_276(text):
    """
    Glyph 276 — Symbolic Frame Fracturer
    Splits a string into alternating character groups.

    Example Input:
    'abcdef'

    Output:
    ['ace', 'bdf']
    """
    return [text[::2], text[1::2]]
