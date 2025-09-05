def lift_spiral(arr):
    """
    Returns cumulative spiral lift of values.

    Parameters:
        arr (List[int]): Base stream.

    Returns:
        List[int]: Accumulated spiral.
    """
    total = 0
    result = []
    for x in arr:
        total += x
        result.append(total)
    return result
