def glyph_120(activation_codes):
    """
    💠 Sorts and returns all valid numerical activation pulses.
    Used in threshold gate sequencing and energy tiering.
    """
    return sorted([c for c in activation_codes if isinstance(c, int)])
