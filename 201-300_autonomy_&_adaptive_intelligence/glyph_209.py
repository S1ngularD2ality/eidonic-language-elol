def glyph_209(seq):
    """
    Glyph 209 — Mirror Polarity Encoder
    Encodes a binary sequence as mirrored polarity (+1, -1).

    Example Input:
    [1, 0, 1]

    Output:
    [1, -1, 1]
    """
    return [1 if x == 1 else -1 for x in seq]
