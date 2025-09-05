# glyph_496 – TIMESTAMP_SYNC
# Synchronize timestamps across all agents

def glyph_496(agent_list, timestamp):
    """
    agent_list: list of agents
    timestamp: float
    Returns: dict of agent:timestamp
    """
    return {a: timestamp for a in agent_list}
