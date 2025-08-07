# glyph_397 – CARRY_BALANCE
# Maintain balance and stability while carrying variable loads

def glyph_397(weight, position, center_of_mass):
    """
    weight: carried object weight
    position: (x, y) robot position
    center_of_mass: (x, y) of system
    Returns: 'adjust left', 'adjust right', or 'balanced'
    """
    if center_of_mass[0] < position[0] - 0.1:
        return "adjust right"
    if center_of_mass[0] > position[0] + 0.1:
        return "adjust left"
    return "balanced"
