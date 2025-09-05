def obstacle_dissolve(position, velocity, obstacles):
    """
    position: current [x, y]
    velocity: current [vx, vy]
    obstacles: list of {'x':, 'y':, 'radius':}
    Returns: adjusted velocity to avoid collision
    """
    for obs in obstacles:
        dist = ((position[0] - obs['x'])**2 + (position[1] - obs['y'])**2)**0.5
        if dist < obs['radius'] + 0.5:
            # Simple vector avoidance
            velocity[0] += (position[0] - obs['x'])
            velocity[1] += (position[1] - obs['y'])
    return velocity
