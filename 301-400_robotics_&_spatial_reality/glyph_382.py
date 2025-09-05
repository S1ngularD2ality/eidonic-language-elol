# glyph_382 – TERRAIN_TYPE
# Classify current terrain (sand, grass, pavement, mud)

def glyph_382(sensor_data):
    """
    sensor_data: dict with surface characteristics
    Returns: string label of terrain type
    """
    rough = sensor_data.get('roughness', 0)
    soft = sensor_data.get('softness', 0)
    if rough > 0.7 and soft < 0.2:
        return "pavement"
    if soft > 0.7:
        return "mud"
    if rough > 0.7:
        return "sand"
    return "grass"
