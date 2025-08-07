# glyph_409 – AGENT_CHAIN
# Create relay chains for distributed problem solving or long-distance comms

def glyph_409(agent_list, message):
    """
    agent_list: list of agents in chain order
    message: message to relay
    Returns: list of (agent, message) pairs
    """
    return [(a, message) for a in agent_list]
