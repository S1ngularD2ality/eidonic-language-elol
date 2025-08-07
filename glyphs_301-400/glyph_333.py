# glyph_333 – ZONE_ALERT
# Detect entry into predefined zones and trigger alerts or behaviors

def glyph_333(position, zones):
    """
    position: (x, y)
    zones: list of dicts with 'name', 'bounds'
    """
    for zone in zones:
        x, y = position
        xmin, xmax, ymin, ymax = zone['bounds']
        if xmin <= x <= xmax and ymin <= y <= ymax:
            return f"Entered zone: {zone['name']}"
    return None
