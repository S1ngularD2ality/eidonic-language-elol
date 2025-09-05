def detect_null_zones(arr):
    """
    Finds positions of symbolic voids (0s).

    Parameters:
        arr (List[int]): Signal array.

    Returns:
        List[int]: Indexes of nulls.
    """
    return [i for i, x in enumerate(arr) if x == 0]
