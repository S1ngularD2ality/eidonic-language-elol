def collapse_nulls(arr):
    """
    Removes all zero entries from a stream.

    Parameters:
        arr (List[int]): Symbol array.

    Returns:
        List[int]: Purged array.
    """
    return [x for x in arr if x != 0]
