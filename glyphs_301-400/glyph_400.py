# glyph_400 – REUNION_CALL
# Broadcast for all kin robots or agents to return to home or rally point

def glyph_400(agent_list, home_position):
    """
    agent_list: list of agent IDs
    home_position: coordinates
    Returns: dict of agent:home_command
    """
    return {agent: f"return to {home_position}" for agent in agent_list}
