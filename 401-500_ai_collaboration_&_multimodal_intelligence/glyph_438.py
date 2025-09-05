# glyph_438 – HARMONIC_VOTE
# Find consensus by harmonic mean of all agent ratings or choices

def glyph_438(ratings):
    """
    ratings: list of numeric ratings
    Returns: harmonic mean
    """
    from statistics import harmonic_mean
    return harmonic_mean(ratings) if ratings else 0
