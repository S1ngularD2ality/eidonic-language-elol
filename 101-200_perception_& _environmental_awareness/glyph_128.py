def glyph_128(frequency_line):
    """
    💠 Replaces all even-indexed frequencies with 0.
    Used to simulate veil disruption or blind-phase pulses.
    """
    return [0 if i % 2 == 0 else x for i, x in enumerate(frequency_line)]
