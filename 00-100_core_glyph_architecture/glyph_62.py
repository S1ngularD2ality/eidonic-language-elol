def entropy_count(arr):
    """
    Counts distinct symbols in array.

    Parameters:
        arr (List[int]): Signal.

    Returns:
        int: Number of unique symbols.
    """
    return len(set(arr))
