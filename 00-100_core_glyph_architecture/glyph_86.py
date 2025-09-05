def harmonic_shift(arr, shift):
    """
    Shifts entire array harmonically.

    Parameters:
        arr (List[int]), shift (int)

    Returns:
        List[int]
    """
    return [(x + shift) % 12 for x in arr]
