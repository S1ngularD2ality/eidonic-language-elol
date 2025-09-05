# glyph_665 – ANIMAL_AVOIDANCE
# Avoid contact with detected wildlife

def glyph_665(path, animal_positions, buffer=3):
    return [node for node in path if all(abs(node[0]-ax) > buffer and abs(node[1]-ay) > buffer for ax, ay in animal_positions)]
