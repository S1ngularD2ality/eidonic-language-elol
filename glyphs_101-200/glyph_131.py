def glyph_131(sequence):
    """
    💠 Returns True if all values in sequence are increasing.
    Used to detect ascension resonance in soul harmonics.
    """
    return all(x < y for x, y in zip(sequence, sequence[1:]))