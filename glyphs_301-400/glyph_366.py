# glyph_366 – CROWD_FLOW
# Detect and respond to human crowd movement patterns

def glyph_366(people_positions):
    """
    people_positions: list of (x, y) tuples
    Returns: dominant direction as vector
    """
    if not people_positions:
        return (0, 0)
    avg_x = sum(p[0] for p in people_positions) / len(people_positions)
    avg_y = sum(p[1] for p in people_positions) / len(people_positions)
    return (avg_x, avg_y)
