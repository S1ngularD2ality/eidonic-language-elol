# glyph_673 – HUMAN_COMFORT_ZONE
# Maintain respectful distance during operation

def glyph_673(human_position, robot_position, min_distance=1.5):
    dx = human_position[0] - robot_position[0]
    dy = human_position[1] - robot_position[1]
    return (dx**2 + dy**2) ** 0.5 >= min_distance
