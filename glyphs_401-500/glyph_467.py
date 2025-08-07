# glyph_467 – AGENT_TAG
# Assign tags or labels to agents for quick grouping/search

def glyph_467(agent_list, tag):
    """
    agent_list: list of agents
    tag: string
    Returns: dict of agent:[tag]
    """
    return {a: [tag] for a in agent_list}
