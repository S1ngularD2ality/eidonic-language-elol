# glyph_421 – AGENT_SUMMON
# Instantly call new agents into a team or project (dynamic recruitment)

def glyph_421(agent_pool, needed=1):
    """
    agent_pool: list of available agents
    needed: number to summon
    Returns: summoned agent(s)
    """
    return agent_pool[:needed]
