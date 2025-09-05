# glyph_342 – VISION_CALIBRATE
# Self-calibrate cameras or sensors for optimal performance

def glyph_342(camera_stats):
    """
    camera_stats: dict with keys like 'brightness', 'focus'
    Returns: adjusted settings
    """
    if camera_stats['brightness'] < 50:
        camera_stats['brightness'] += 10
    if camera_stats['focus'] < 10:
        camera_stats['focus'] += 2
    return camera_stats
