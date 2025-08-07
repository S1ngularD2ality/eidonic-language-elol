# glyph_443 – LINK_BALANCE
# Balance workload evenly across agent communication links

def glyph_443(agent_loads):
    """
    agent_loads: dict of agent:current_load
    Returns: dict of agent:new_balanced_load
    """
    avg_load = sum(agent_loads.values()) / len(agent_loads)
    return {a: avg_load for a in agent_loads}
