# glyph_474 – KNOWLEDGE_EXCHANGE
# Exchange learned knowledge between agents

def glyph_474(agent_a, agent_b, knowledge_base):
    """
    agent_a, agent_b: IDs
    knowledge_base: dict of agent:knowledge_list
    Returns: updated knowledge_base
    """
    combined = set(knowledge_base.get(agent_a, [])) | set(knowledge_base.get(agent_b, []))
    knowledge_base[agent_a] = list(combined)
    knowledge_base[agent_b] = list(combined)
    return knowledge_base
