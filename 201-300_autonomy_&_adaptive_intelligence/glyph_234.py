def glyph_234(timeline):
    """
    Glyph 234 — Temporal Collapse Gate
    Flattens repeating future echoes from timeline sequences.

    Example Input:
    [1, 2, 3, 3, 3]

    Output:
    [1, 2, 3]
    """
    return list(dict.fromkeys(timeline))
