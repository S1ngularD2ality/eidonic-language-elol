# glyph_959 – CONSENSUS_QUORUM_VOTE
"""
Consensus Quorum Vote (Threshold Accept)

Aggregates signed votes (hash digests here) and declares acceptance when
a threshold t of n members agree.

APIs:
- accept(votes: List[bytes], t: int) -> bool
"""

def accept(votes: list[bytes], t: int) -> bool:
    from collections import Counter
    c = Counter(votes)
    return any(count >= t for count in c.values())
