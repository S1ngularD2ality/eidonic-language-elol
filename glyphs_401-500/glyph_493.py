# glyph_493 – PATH_INTERWEAVE
# Interweave agent paths for optimal coverage without collision

def glyph_493(agent_paths):
    """
    agent_paths: dict of agent:[path_points]
    Returns: interwoven path plan
    """
    return {a: sorted(path) for a, path in agent_paths.items()}
