# glyph_407 – VOTE_SPLIT
# Split tasks or resources based on collective voting/poll

def glyph_407(votes):
    """
    votes: dict of agent:choice
    Returns: winning choice(s)
    """
    from collections import Counter
    tally = Counter(votes.values())
    max_votes = max(tally.values())
    return [k for k, v in tally.items() if v == max_votes]
