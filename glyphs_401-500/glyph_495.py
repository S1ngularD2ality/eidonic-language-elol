# glyph_495 – AGENT_SHADOW
# Assign a shadow/backup agent to each active agent

def glyph_495(agent_list):
    """
    agent_list: list of agents
    Returns: dict of agent:shadow_agent
    """
    return {agent_list[i]: agent_list[(i+1) % len(agent_list)] for i in range(len(agent_list))}
