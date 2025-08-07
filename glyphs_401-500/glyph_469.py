# glyph_469 – AGENT_PATH
# Assign unique navigation paths to each agent to avoid collisions

def glyph_469(agent_list, path_templates):
    """
    agent_list: list of agents
    path_templates: list of paths
    Returns: dict of agent:path
    """
    return {agent: path_templates[i % len(path_templates)] for i, agent in enumerate(agent_list)}
