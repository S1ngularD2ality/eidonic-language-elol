def inverse_cascade(arr):
    """
    Reverses sequence and lowers magnitude.

    Returns:
        List[int]
    """
    return [x * -1 for x in arr[::-1]]
