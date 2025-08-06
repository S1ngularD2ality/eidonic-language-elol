def glyph_210(seq, shift):
    """
    Glyph 210 — Temporal Shift Operator
    Shifts a sequence cyclically in time by 'shift' units.

    Example Input:
    ([1, 2, 3, 4], 2)

    Output:
    [3, 4, 1, 2]
    """
    l = len(seq)
    return seq[shift % l:] + seq[:shift % l]
