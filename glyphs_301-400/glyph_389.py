# glyph_389 – GPS_LOCK
# Lock current position to GPS and prevent drift/loss

def glyph_389(gps_data, lock=True):
    """
    gps_data: (lat, lon)
    lock: bool, if True lock, if False unlock
    Returns: locked position or None
    """
    return gps_data if lock else None
