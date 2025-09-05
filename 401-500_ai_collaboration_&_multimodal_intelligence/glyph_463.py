# glyph_463 – CYCLE_ROTATE
# Rotate operational cycles between agents to maintain efficiency

def glyph_463(agent_cycles):
    """
    agent_cycles: dict of agent:cycle_value
    Returns: rotated dict
    """
    agents = list(agent_cycles.keys())
    values = list(agent_cycles.values())
    rotated_values = values[1:] + values[:1]
    return dict(zip(agents, rotated_values))
