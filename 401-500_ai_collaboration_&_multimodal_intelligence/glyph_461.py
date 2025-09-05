# glyph_461 – CLUSTER_FORM
# Group agents into clusters based on proximity or similarity

def glyph_461(agent_positions, max_distance):
    """
    agent_positions: dict of agent:(x, y)
    max_distance: float
    Returns: list of clusters (list of agents)
    """
    clusters = []
    visited = set()

    for agent, pos in agent_positions.items():
        if agent in visited:
            continue
        cluster = [agent]
        visited.add(agent)
        for other, other_pos in agent_positions.items():
            if other not in visited:
                dist = ((pos[0] - other_pos[0])**2 + (pos[1] - other_pos[1])**2) ** 0.5
                if dist <= max_distance:
                    cluster.append(other)
                    visited.add(other)
        clusters.append(cluster)
    return clusters
