# glyph_718 – AI_CONSENSUS_PROTOCOL
# N-of-M consensus on proposed actions.

from collections import Counter

def glyph_718(votes, quorum=None):
    """
    votes: list[str] proposed actions
    quorum: minimum number to accept; default majority
    Returns: {'decision': str|None, 'counts': {action:count}}
    """
    tally = Counter(votes)
    action, count = (tally.most_common(1)[0] if tally else (None, 0))
    q = quorum or (len(votes)//2 + 1)
    decision = action if count >= q else None
    return {"decision": decision, "counts": dict(tally), "quorum": q}
