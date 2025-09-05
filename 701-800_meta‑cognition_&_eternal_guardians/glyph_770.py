# glyph_770 – CONTINUOUS_HARMONIC_BALANCE
# Keeps multi-agent systems in cooperation balance.

def glyph_770(agent_states):
    """
    agent_states: dict agent->cooperation_score
    Returns: balanced_scores
    """
    max_score = max(agent_states.values()) or 1
    return {agent: score / max_score for agent, score in agent_states.items()}
