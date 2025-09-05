def discrete_shift(arr):
    """
    Encodes array by computing forward deltas between adjacent elements.

    Parameters:
        arr (List[int]): Symbolic timeline.

    Returns:
        List[int]: Shift values.
    """
    return [arr[i+1] - arr[i] for i in range(len(arr)-1)]
