# glyph_838 – SYMMETRY_BREAKER
# Add tiny deterministic perturbations to break ties/symmetries.

def glyph_838(values, epsilon=1e-9):
    """
    Returns new list with ε*(index+1) added to each value.
    """
    return [v + epsilon*(i+1) for i, v in enumerate(values)]
