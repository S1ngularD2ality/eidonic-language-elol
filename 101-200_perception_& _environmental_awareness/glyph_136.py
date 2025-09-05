def glyph_136(values):
    """
    💠 Sums all values not divisible by 3.
    Ideal for bias removal in triadic loop simulations.
    """
    return sum(x for x in values if x % 3 != 0)