# glyph_489 – HEARTBEAT_MONITOR
# Monitor and alert if any agent's heartbeat stops

def glyph_489(agent_heartbeats):
    """
    agent_heartbeats: dict of agent:last_heartbeat_timestamp
    Returns: list of agents offline
    """
    import time
    now = time.time()
    return [a for a, ts in agent_heartbeats.items() if now - ts > 5]
