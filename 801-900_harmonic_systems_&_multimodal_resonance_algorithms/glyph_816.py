# glyph_816 – OCTAVE_HARMONIC_RESOLVER
# Quantize values to nearest tenth (simple harmonic rounding).

def glyph_816(values):
    """
    Returns list rounded to 0.1 steps.
    """
    return [round(float(v), 1) for v in values]
