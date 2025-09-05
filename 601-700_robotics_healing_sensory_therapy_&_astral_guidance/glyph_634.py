# glyph_634 – CROWD_SAFETY_PATH
# Choose widest possible path in crowded areas

def glyph_634(paths):
    return max(paths, key=lambda p: sum(1 for step in p if step.get('space', 0) > 1.5))
