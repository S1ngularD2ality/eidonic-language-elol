# glyph_377 – BEACON_TRACK
# Lock onto and follow beacon signals for homing or rendezvous

def glyph_377(beacon_data):
    """
    beacon_data: dict of beacon_id:signal_strength
    Returns: id of strongest beacon
    """
    return max(beacon_data, key=beacon_data.get)
