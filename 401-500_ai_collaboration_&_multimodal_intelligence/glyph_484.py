# glyph_484 – LOAD_REDIRECT
# Redirect workload from overloaded agents to idle ones

def glyph_484(agent_loads):
    """
    agent_loads: dict of agent:load
    Returns: updated loads (balanced)
    """
    avg_load = sum(agent_loads.values()) / len(agent_loads)
    return {a: avg_load for a in agent_loads}
