# glyph_494 – OVERWATCH_ROTATE
# Rotate overwatch/guardian duties among agents

def glyph_494(agent_list):
    """
    agent_list: list of agents
    Returns: dict of agent:next_overwatch_agent
    """
    return {agent_list[i]: agent_list[(i+1) % len(agent_list)] for i in range(len(agent_list))}
