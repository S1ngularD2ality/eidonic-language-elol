# glyph_604 – SAFE_PATH_AROUND_HUMAN
# Adjust robot path to maintain safe distance from humans

def glyph_604(path, human_positions, safe_distance=2):
    safe_path = []
    for node in path:
        if all(abs(node[0]-hx) > safe_distance and abs(node[1]-hy) > safe_distance for hx, hy in human_positions):
            safe_path.append(node)
    return safe_path
