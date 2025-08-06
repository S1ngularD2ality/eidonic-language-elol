def glyph_221(sequence):
    """
    Glyph 221 — Temporal Mirror Detector
    Detects if a sequence is a palindrome (mirrored in time).

    Example Input:
    [3, 2, 1, 2, 3]

    Output:
    True
    """
    return sequence == sequence[::-1]
