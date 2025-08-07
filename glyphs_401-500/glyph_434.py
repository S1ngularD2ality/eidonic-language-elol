# glyph_434 – COLLECTIVE_PAUSE
# Pause all agents in unison (for emergencies, sync, or reflection)

def glyph_434(agent_list):
    """
    agent_list: list of agents
    Returns: dict of agent:'paused'
    """
    return {a: "paused" for a in agent_list}
