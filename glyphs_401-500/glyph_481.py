# glyph_481 – AGENT_PING
# Ping all agents to confirm presence and latency

def glyph_481(agent_list):
    """
    agent_list: list of agents
    Returns: dict of agent:latency_ms (simulated)
    """
    import random
    return {a: random.randint(1, 100) for a in agent_list}
