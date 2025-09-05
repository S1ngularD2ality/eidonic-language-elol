# glyph_627 – HUMAN_FOLLOW_MODE
# Maintain safe following distance behind a human

def glyph_627(human_path, follow_distance=3):
    return [(x, y) for x, y in human_path if human_path.index((x, y)) >= follow_distance]
