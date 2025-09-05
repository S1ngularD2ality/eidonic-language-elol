# glyph_821 – TORUS_COORDINATE_MAPPER
# Wrap 2D coordinates onto a torus (donut topology) with modular edges.

def glyph_821(x, y, width, height):
    """
    Returns (x', y') where both wrap seamlessly across edges.
    """
    x_prime = x % width
    y_prime = y % height
    return (x_prime, y_prime)
