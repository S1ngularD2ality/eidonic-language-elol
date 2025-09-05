# glyph_605 – ENERGY_EFFICIENT_ROUTE
# Optimize route for minimum energy usage

def glyph_605(path, energy_map):
    return sum(energy_map.get(node, 1) for node in path)
