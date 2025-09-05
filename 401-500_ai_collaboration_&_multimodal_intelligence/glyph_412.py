# glyph_412 – AGENT_FOCUS
# Focus collective attention/resources on a target or priority

def glyph_412(agent_list, target):
    """
    agent_list: list of agents
    target: focus subject
    Returns: dict of agent:focus_target
    """
    return {a: target for a in agent_list}
