def harmonic_bias(decision, environment):
    """
    Enforces non-harmful action override.
    """
    if 'living_being' in environment and decision == 'move_through':
        return 'reroute'
    return decision
