# glyph_775 – CONSENSUS_DECISION_ENGINE
# Requires multiple sub-systems to agree on an action.

def glyph_775(votes):
    """
    votes: list of True/False
    Returns: bool decision
    """
    return sum(votes) > len(votes) // 2
