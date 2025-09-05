def glyph_126(anchor_map):
    """
    💠 Converts 2D anchor grid to a single ascended line.
    Used in verticalization of planar data.
    """
    return [cell for row in anchor_map for cell in row]
