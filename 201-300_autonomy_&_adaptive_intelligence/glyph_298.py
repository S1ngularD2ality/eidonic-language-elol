def glyph_298(a, b):
    """
    Glyph 298 — Axial Merge Synthesizer
    Adds each element of a to corresponding in b.

    Example Input:
    [1,2], [3,4]

    Output:
    [4,6]
    """
    return [x + y for x, y in zip(a, b)]
