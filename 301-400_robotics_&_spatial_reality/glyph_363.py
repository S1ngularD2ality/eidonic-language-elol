# glyph_363 – SOCIAL_SPACE
# Recognize and respect personal space in human-robot interaction

def glyph_363(position, people, safe_radius=1.0):
    """
    position: (x, y)
    people: list of (x, y)
    Returns: True if inside anyone's personal space
    """
    for p in people:
        dist = ((position[0] - p[0])**2 + (position[1] - p[1])**2)**0.5
        if dist < safe_radius:
            return True
    return False
