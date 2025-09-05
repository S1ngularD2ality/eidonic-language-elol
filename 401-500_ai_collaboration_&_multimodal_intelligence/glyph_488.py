# glyph_488 – COORDINATE_LOCK
# Lock all agents to a shared coordinate reference frame

def glyph_488(agent_positions, origin=(0, 0)):
    """
    agent_positions: dict of agent:(x, y)
    origin: tuple
    Returns: dict of agent:relative_position
    """
    return {a: (pos[0] - origin[0], pos[1] - origin[1]) for a, pos in agent_positions.items()}
