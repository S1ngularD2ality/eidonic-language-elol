# glyph_337 – EDGE_FINDER
# Detect and outline physical edges in a scene for safe navigation

def glyph_337(image):
    """
    image: 2D array
    Returns: list of edge coordinates
    """
    # Pseudo-logic for clarity
    edges = [(x, y) for x in range(len(image)) for y in range(len(image[0])) if image[x][y] > 128]
    return edges
