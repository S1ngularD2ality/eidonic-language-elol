def symmetric_diffuse(arr):
    """
    Reflects a symbolic array into symmetric form.

    Parameters:
        arr (List[int]): Original array.

    Returns:
        List[int]: Forward + reversed pattern.
    """
    return arr + arr[::-1]
