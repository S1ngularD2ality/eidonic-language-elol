# glyph_471 – RING_VOTE
# Conduct a voting process in ring order to ensure fairness

def glyph_471(agent_list, choices):
    """
    agent_list: list of agents
    choices: dict of agent:choice
    Returns: most voted choice
    """
    from collections import Counter
    vote_count = Counter(choices.values())
    return vote_count.most_common(1)[0][0]
