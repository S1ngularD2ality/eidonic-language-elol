def overlay_stream(*grids):
    """
    Overlays multiple symbolic frames.

    Returns:
        List[List[int]]
    """
    return [[sum(values) for values in zip(*rows)] for rows in zip(*grids)]
