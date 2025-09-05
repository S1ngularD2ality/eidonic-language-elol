# glyph_499 – FAILOVER_PATH
# Assign backup paths in case of route failure

def glyph_499(agent_routes, backup_routes):
    """
    agent_routes: dict of agent:route
    backup_routes: dict of agent:backup_route
    Returns: dict of agent:(route, backup_route)
    """
    return {a: (agent_routes.get(a), backup_routes.get(a)) for a in agent_routes}
