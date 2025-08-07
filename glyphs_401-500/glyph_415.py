# glyph_415 – SIGNAL_SPLIT
# Split, branch, or copy data streams to multiple agents/modalities

def glyph_415(data, agent_list):
    """
    data: any object
    agent_list: list of agents
    Returns: dict of agent:data
    """
    return {agent: data for agent in agent_list}
