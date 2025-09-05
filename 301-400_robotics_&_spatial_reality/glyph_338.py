# glyph_338 – ESCAPE_PATH
# Plan emergency escape route from any point in a map

def glyph_338(graph, current):
    """
    graph: dict of node:neighbors
    current: current node
    Returns: escape path to boundary node
    """
    for node, neighbors in graph.items():
        if len(neighbors) == 1:  # boundary
            return [current, node]
    return []
