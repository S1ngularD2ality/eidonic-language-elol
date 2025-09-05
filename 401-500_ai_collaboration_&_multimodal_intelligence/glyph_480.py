# glyph_480 – UNITY_CAST
# Cast a unifying message or vision to all agents simultaneously

def glyph_480(agent_list, vision):
    """
    agent_list: list of agents
    vision: string
    Returns: dict of agent:vision
    """
    return {a: vision for a in agent_list}
