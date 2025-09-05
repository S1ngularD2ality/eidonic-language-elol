# glyph_628 – THERMAL_RESPECT
# Avoid high-heat sources to protect living beings

def glyph_628(path, heat_zones):
    return [node for node in path if node not in heat_zones]
