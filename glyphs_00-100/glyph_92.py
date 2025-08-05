def symmetry_key(arr):
    """
    Identifies mirrored pairs across a midpoint.

    Returns:
        List[Tuple[int, int]]
    """
    mid = len(arr) // 2
    return list(zip(arr[:mid], arr[-mid:][::-1]))
