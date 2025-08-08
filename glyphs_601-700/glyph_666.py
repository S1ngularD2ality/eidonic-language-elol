# glyph_666 – SAFETY_ZONE_CREATE
# Mark a temporary safety zone around humans

def glyph_666(human_location, radius=2):
    return [(human_location[0]+dx, human_location[1]+dy) for dx in range(-radius, radius+1) for dy in range(-radius, radius+1)]
