# glyph_442 – SWARM_MERGE
# Merge multiple agent swarms into a single coordinated unit

def glyph_442(*swarms):
    """
    swarms: any number of lists of agents
    Returns: merged unique list of agents
    """
    merged = set()
    for swarm in swarms:
        merged.update(swarm)
    return list(merged)
