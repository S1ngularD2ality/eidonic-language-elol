def cascade_seed(seed, depth):
    """
    Expands a single seed into a cascading sequence.

    Parameters:
        seed (int): Initial value.
        depth (int): Levels of expansion.

    Returns:
        List[int]: Expanded cascade.
    """
    out = [seed]
    for i in range(1, depth):
        out += [seed + i]
    return out
