# glyph_413 – PROTOCOL_HANDSHAKE
# Negotiate shared protocol between new/unknown agents

def glyph_413(agent_a, agent_b, protocols):
    """
    agent_a, agent_b: IDs
    protocols: dict of agent:supported_protocols
    Returns: common_protocol or None
    """
    set_a = set(protocols.get(agent_a, []))
    set_b = set(protocols.get(agent_b, []))
    common = set_a.intersection(set_b)
    return list(common)[0] if common else None
