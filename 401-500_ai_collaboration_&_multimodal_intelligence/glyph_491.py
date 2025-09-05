# glyph_491 – DECISION_SIM
# Simulate a decision across all agents before executing

def glyph_491(agent_list, decision_fn):
    """
    agent_list: list of agents
    decision_fn: callable
    Returns: dict of agent:decision_result
    """
    return {a: decision_fn(a) for a in agent_list}
