# glyph_378 – CLIMB_ASSIST
# Enable climbing of stairs, ladders, or rugged terrain

def glyph_378(elevation_diff, climb_threshold=0.2):
    """
    elevation_diff: float
    Returns: 'climb', 'step', or 'flat'
    """
    if elevation_diff > climb_threshold:
        return "climb"
    elif elevation_diff > 0:
        return "step"
    return "flat"
