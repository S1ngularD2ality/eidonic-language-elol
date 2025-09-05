# glyph_352 – INFRARED_VISION
# See and map heat sources and obstacles with IR sensors

def glyph_352(ir_data):
    """
    ir_data: dict of location:temp
    Returns: hot_spots list
    """
    return [loc for loc, t in ir_data.items() if t > 35]
