# glyph_450 – AGENT_RESURRECT
# Restore a disconnected or dormant agent to active status

def glyph_450(agent, status_log):
    """
    agent: string
    status_log: dict of agent:status
    Returns: updated status_log
    """
    status_log[agent] = "active"
    return status_log
