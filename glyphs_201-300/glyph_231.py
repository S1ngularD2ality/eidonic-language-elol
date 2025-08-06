def glyph_231(sequence, k):
    """
    Glyph 231 — Resonant Cycle Shifter
    Rotates a sequence right by k, completing a resonance cycle.

    Example Input:
    ([1, 2, 3, 4], 2)

    Output:
    [3, 4, 1, 2]
    """
    k = k % len(sequence)
    return sequence[-k:] + sequence[:-k]
