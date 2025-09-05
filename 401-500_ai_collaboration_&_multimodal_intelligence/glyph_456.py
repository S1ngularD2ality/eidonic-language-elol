# glyph_456 – SWARM_ALERT
# Send an emergency alert to all members of a swarm

def glyph_456(swarm, alert_msg):
    """
    swarm: list of agents
    alert_msg: string
    Returns: dict of agent:alert_msg
    """
    return {a: alert_msg for a in swarm}
