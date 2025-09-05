# glyph_444 – DECISION_MAP
# Map decisions to responsible agents for accountability tracking

def glyph_444(decisions):
    """
    decisions: list of (decision, agent)
    Returns: dict of decision:agent
    """
    return {d: a for d, a in decisions}
