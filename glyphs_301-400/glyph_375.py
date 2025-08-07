# glyph_375 – PROXIMITY_ALERT
# Detect close obstacles and trigger avoidance or alerts

def glyph_375(distance_data, threshold=0.5):
    """
    distance_data: dict of sensor_id:distance
    Returns: list of sensors below threshold
    """
    return [sid for sid, d in distance_data.items() if d < threshold]
