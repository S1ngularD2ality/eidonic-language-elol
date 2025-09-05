def collapse_threshold(arr, limit):
    """
    Filters out values that exceed a stability threshold.

    Parameters:
        arr (List[int]): Input sequence.
        limit (int): Maximum allowed symbolic value.

    Returns:
        List[int]: Filtered sequence.
    """
    return [x for x in arr if x <= limit]
