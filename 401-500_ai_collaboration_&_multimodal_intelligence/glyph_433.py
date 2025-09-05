# glyph_433 – SHARED_AWARENESS
# Make all agents aware of a new context, variable, or environmental change

def glyph_433(agent_list, context):
    """
    agent_list: list of agents
    context: any
    Returns: dict of agent:context
    """
    return {a: context for a in agent_list}
