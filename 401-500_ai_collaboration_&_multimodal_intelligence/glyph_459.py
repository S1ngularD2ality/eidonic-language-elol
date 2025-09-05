# glyph_459 – MEDIATOR
# Assign a neutral agent to mediate conflicts

def glyph_459(agent_list):
    """
    agent_list: list of agents
    Returns: mediator agent (middle of list)
    """
    if not agent_list:
        return None
    return agent_list[len(agent_list) // 2]
