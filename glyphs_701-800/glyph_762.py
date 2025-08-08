# glyph_762 – DISTRIBUTED_SELF_CHECK
# Coordinates self-check across multiple nodes.

def glyph_762(nodes):
    """
    nodes: list of callables returning health status (bool)
    Returns: dict of node_id -> status
    """
    return {i: node() for i, node in enumerate(nodes)}
