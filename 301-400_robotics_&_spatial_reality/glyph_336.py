# glyph_336 – ENERGY_SENSE
# Detect and record environmental energy sources (power outlets, sunlight, wireless)

def glyph_336(energy_data):
    """
    energy_data: dict with source:type, strength
    Returns: sorted energy sources by strength
    """
    return sorted(energy_data.items(), key=lambda x: x[1]['strength'], reverse=True)
