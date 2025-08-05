def glyph_139(temporal_grid):
    """
    💠 Subtracts row index from each row value.
    Used in echo pattern temporal reversal processing.
    """
    return [[cell - i for cell in row] for i, row in enumerate(temporal_grid)]