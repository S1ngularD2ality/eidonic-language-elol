# glyph_437 – CIRCLE_LINK
# Close a collaboration loop—every agent connects to the next in a ring

def glyph_437(agent_list):
    """
    agent_list: list of agents
    Returns: list of (from_agent, to_agent) forming a ring
    """
    return [(agent_list[i], agent_list[(i+1)%len(agent_list)]) for i in range(len(agent_list))]
