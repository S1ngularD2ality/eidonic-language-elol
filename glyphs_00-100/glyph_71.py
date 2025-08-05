def boundary_clamp(arr, low, high):
    """
    Restrains values within bounds.

    Parameters:
        arr (List[int]), low (int), high (int)

    Returns:
        List[int]: Clamped array.
    """
    return [min(max(x, low), high) for x in arr]
