def equalize_temperature(arr):
    """
    Normalizes all values to average.

    Parameters:
        arr (List[int]): Signal array.

    Returns:
        List[int]: Equalized signal.
    """
    if not arr: return []
    avg = sum(arr) // len(arr)
    return [avg] * len(arr)
