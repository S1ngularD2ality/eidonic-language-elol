def glyph_281(a, b, c):
    """
    Glyph 281 — Tri-Spiral Combiner
    Interlaces three lists into one spiraled stream.

    Example Input:
    [1,2], [3,4], [5,6]

    Output:
    [1,3,5,2,4,6]
    """
    return [x for trio in zip(a, b, c) for x in trio]
