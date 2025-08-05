def glyph_127(gateways):
    """
    💠 Returns gateway index positions with value ‘1’.
    Interprets active nodes in the ascension lattice.
    """
    return [i for i, x in enumerate(gateways) if x == 1]
