def interlock_merge(a, b):
    """
    Merges two arrays in interlocked fashion.

    Parameters:
        a (List[int]), b (List[int])

    Returns:
        List[int]: Interlocked merge.
    """
    return [x for pair in zip(a, b) for x in pair]
