def drift_pairs(arr):
    """
    Identifies gradient-based pairs in a sequence where the difference is 1 or 2.

    Parameters:
        arr (List[int]): A list of integers to evaluate for gradient shifts.

    Returns:
        List[Tuple[int, int]]: A list of tuple pairs reflecting slight changes in values.
    """
    return [(arr[i], arr[i+1]) for i in range(len(arr)-1) if arr[i+1] - arr[i] in (1, 2)]
