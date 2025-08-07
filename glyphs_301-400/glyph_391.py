# glyph_391 – DEPTH_LOCK
# Lock and maintain distance from a target object or surface

def glyph_391(distance, set_point=1.0, tolerance=0.05):
    """
    distance: current distance to target
    set_point: desired distance
    tolerance: allowed deviation
    Returns: 'move closer', 'move back', or 'hold'
    """
    if distance < set_point - tolerance:
        return "move back"
    elif distance > set_point + tolerance:
        return "move closer"
    return "hold"
