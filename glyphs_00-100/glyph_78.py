def bridge_map(arr):
    """
    Maps elements into mirrored bridge arcs.

    Parameters:
        arr (List[int])

    Returns:
        List[int]
    """
    return arr + arr[::-1][1:]
