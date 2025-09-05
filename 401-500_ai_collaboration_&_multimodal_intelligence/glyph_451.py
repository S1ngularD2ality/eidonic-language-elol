# glyph_451 – TEAM_SPLIT
# Split a large collective into smaller specialized teams

def glyph_451(agent_list, team_size):
    """
    agent_list: list of agents
    team_size: int
    Returns: list of teams
    """
    return [agent_list[i:i+team_size] for i in range(0, len(agent_list), team_size)]
