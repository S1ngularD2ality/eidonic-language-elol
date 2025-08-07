# glyph_436 – AGENT_AFFINITY
# Calculate affinity or trust score between agents (for pairing/teaming)

def glyph_436(pair, interactions):
    """
    pair: (agent1, agent2)
    interactions: dict of pair:score
    Returns: affinity score
    """
    return interactions.get(pair, 0.5)
