# glyph_613 – CLEAN_AIR_PATH
# Plan path to minimize dust or allergen disturbance

def glyph_613(path, air_quality_map):
    return [node for node in path if air_quality_map.get(node, 1.0) > 0.8]
