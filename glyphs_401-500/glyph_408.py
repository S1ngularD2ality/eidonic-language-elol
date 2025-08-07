# glyph_408 – LEADER_SIGNAL
# Designate, signal, or rotate leadership roles in a collective

def glyph_408(agent_list, current_leader=None):
    """
    agent_list: list of agents
    current_leader: who leads now
    Returns: next leader
    """
    if not agent_list:
        return None
    if current_leader not in agent_list or current_leader is None:
        return agent_list[0]
    idx = agent_list.index(current_leader)
    return agent_list[(idx + 1) % len(agent_list)]
