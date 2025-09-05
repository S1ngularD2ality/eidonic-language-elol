# glyph_446 – ALLIANCE_FORGE
# Form an alliance between separate agent collectives

def glyph_446(collective_a, collective_b):
    """
    collective_a: list
    collective_b: list
    Returns: merged alliance
    """
    return list(set(collective_a + collective_b))
