# glyph_617 – SAFE_CARRY_PATH
# Plan carrying route to avoid spills or damage

def glyph_617(path, stability_map):
    return [node for node in path if stability_map.get(node, 1.0) > 0.9]
