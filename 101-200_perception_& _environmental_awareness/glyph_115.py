def glyph_115(pattern_ring):
    """
    💠 Creates a mirrored energy loop.
    Appends the inverse of the ring to its origin.
    """
    return pattern_ring + pattern_ring[::-1]
