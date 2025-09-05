# glyph_402 – COLLAB_ORBIT
# Assign and rotate collaborative roles among agents for distributed teamwork

def glyph_402(agent_list):
    """
    agent_list: list of agent names/IDs
    Returns: new role assignments (rotated order)
    """
    if agent_list:
        return agent_list[1:] + [agent_list[0]]
    return []
