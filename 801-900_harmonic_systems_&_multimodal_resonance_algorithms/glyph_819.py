# glyph_819 – HEXAGONAL_RESOURCE_GRID
# Honeycomb allocation: partition into 6 interleaved lanes.

def glyph_819(resources):
    """
    Returns list of 6 lists, each lane is resources[i::6].
    """
    return [list(resources[i::6]) for i in range(6)]
