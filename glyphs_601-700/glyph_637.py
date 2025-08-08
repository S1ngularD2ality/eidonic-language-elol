# glyph_637 – DUST_CONTROL_PATH
# Navigate to minimize dust disturbance

def glyph_637(path, dust_map):
    return [node for node in path if dust_map.get(node, 0) < 0.3]
