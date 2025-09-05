# glyph_492 – RECALL_SYNC
# Sync all agents’ recall memory with the latest version

def glyph_492(agent_memories):
    """
    agent_memories: dict of agent:memory_data
    Returns: dict of agent:shared_memory
    """
    latest = list(agent_memories.values())[0] if agent_memories else None
    return {a: latest for a in agent_memories}
