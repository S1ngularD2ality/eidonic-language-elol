# glyph_652 – FLOOD_ZONE_AVOID
# Avoid low-lying areas prone to flooding

def glyph_652(path, flood_zones):
    return [node for node in path if node not in flood_zones]
