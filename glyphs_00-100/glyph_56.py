def expand_blocks(arr, reps):
    """
    Repeats each symbol a number of times.

    Parameters:
        arr (List[int]): Base pattern.
        reps (int): Number of repetitions.

    Returns:
        List[int]: Expanded sequence.
    """
    return [x for x in arr for _ in range(reps)]
