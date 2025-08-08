# glyph_814 – PYRAMID_ENERGY_STABILIZER
# Flatten load values to a shared base (centroid) to avoid spikes.

def glyph_814(load_values):
    """
    Returns a list where each entry equals the mean of inputs.
    """
    if not load_values:
        return []
    base = sum(load_values) / len(load_values)
    return [base for _ in load_values]
