# glyph_420 – INTENTION_HARMONIZER
# Align and synchronize intentions or goals for smooth collaboration

def glyph_420(agent_goals):
    """
    agent_goals: dict of agent:goal
    Returns: harmonized goal (most common or consensus)
    """
    from collections import Counter
    goals = list(agent_goals.values())
    return Counter(goals).most_common(1)[0][0]
