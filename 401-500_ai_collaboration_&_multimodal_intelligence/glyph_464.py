# glyph_464 – INFLUENCE_MAP
# Map influence or leadership strength within a collective

def glyph_464(influence_scores):
    """
    influence_scores: dict of agent:score
    Returns: agent with highest influence
    """
    return max(influence_scores, key=influence_scores.get)
