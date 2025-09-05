def glyph_225(values, divisor):
    """
    Glyph 225 — Harmonic Modulator
    Applies modulo to align values to harmonic threshold.

    Example Input:
    ([5, 12, 19], 7)

    Output:
    [5, 5, 5]
    """
    return [x % divisor for x in values]
