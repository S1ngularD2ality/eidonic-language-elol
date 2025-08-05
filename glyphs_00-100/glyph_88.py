def displacement_tracker(a, b):
    """
    Calculates delta between aligned reflections.

    Returns:
        List[int]
    """
    return [bi - ai for ai, bi in zip(a, b)]
