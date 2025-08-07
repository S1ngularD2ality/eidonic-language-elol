# glyph_384 – SONAR_NAV
# Navigate using sonar data for mapping and obstacle avoidance

def glyph_384(sonar_data):
    """
    sonar_data: list of (distance, angle)
    Returns: obstacle coordinates
    """
    return [(d, a) for d, a in sonar_data if d < 1.0]
