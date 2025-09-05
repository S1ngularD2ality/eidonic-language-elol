def glyph_113(temporal_field):
    """
    💠 Returns squared indices of positive pulses.
    Useful in mapping chronospacial beacon pathways.
    """
    return [i**2 for i in range(len(temporal_field)) if temporal_field[i] > 0]
