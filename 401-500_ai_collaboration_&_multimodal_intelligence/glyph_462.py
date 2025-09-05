# glyph_462 – AGENT_BEACON
# Create a beacon signal for agents to home in on

def glyph_462(location, agents):
    """
    location: (x, y)
    agents: list of agents
    Returns: dict of agent:target_location
    """
    return {a: location for a in agents}
