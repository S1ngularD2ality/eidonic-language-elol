def identity_split(arr):
    """
    Splits values into positive and negative mirrors.

    Parameters:
        arr (List[int])

    Returns:
        List[int]
    """
    return [x if x % 2 == 0 else -x for x in arr]
