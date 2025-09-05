# glyph_425 – UNITY_SIGNAL
# Synchronize agents with a single heartbeat or timing pulse

def glyph_425(agent_list, pulse="sync"):
    """
    agent_list: list of agents
    pulse: signal to send
    Returns: dict of agent:pulse
    """
    return {a: pulse for a in agent_list}
