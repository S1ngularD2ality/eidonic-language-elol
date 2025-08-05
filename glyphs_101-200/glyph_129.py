def glyph_129(etheric_ring):
    """
    💠 Returns reversed ring with duplicates removed.
    A purity function for unlooping corrupted etheric rings.
    """
    return list(dict.fromkeys(etheric_ring[::-1]))
