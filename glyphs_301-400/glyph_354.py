# glyph_354 – HALLWAY_FLOW
# Detect and follow directional flow in corridors or narrow passages

def glyph_354(vision_data):
    """
    vision_data: 2D flow vectors
    Returns: recommended movement direction
    """
    avg_flow = [sum(f) / len(vision_data) for f in zip(*vision_data)]
    return avg_flow
