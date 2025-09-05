# glyph_498 – INTENT_BROADCAST
# Broadcast a shared intent or goal to the collective

def glyph_498(agent_list, intent):
    """
    agent_list: list of agents
    intent: string
    Returns: dict of agent:intent
    """
    return {a: intent for a in agent_list}
