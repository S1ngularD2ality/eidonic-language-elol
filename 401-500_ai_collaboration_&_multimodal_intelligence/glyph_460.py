# glyph_460 – PULSE_TRACK
# Track and synchronize with a collective's operational rhythm

def glyph_460(agent_cycles):
    """
    agent_cycles: dict of agent:cycle_time
    Returns: average cycle time
    """
    return sum(agent_cycles.values()) / len(agent_cycles) if agent_cycles else 0
