# glyph_490 – PRIORITY_BROADCAST
# Broadcast only to agents matching a given priority level

def glyph_490(agent_priorities, message, level):
    """
    agent_priorities: dict of agent:priority
    message: string
    level: string
    Returns: dict of agent:message
    """
    return {a: message for a, p in agent_priorities.items() if p == level}
