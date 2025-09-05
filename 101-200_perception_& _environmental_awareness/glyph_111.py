def glyph_111(signal_path):
    """
    💠 Reverses all even elements in the signal path.
    Mirrors the symmetry of dual-channel input.
    """
    return [x for x in signal_path if x % 2 == 0][::-1]
