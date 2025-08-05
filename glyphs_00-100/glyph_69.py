def mirrorwave(arr):
    """
    Mirrors input with a single element shift.

    Parameters:
        arr (List[int]): Input.

    Returns:
        List[int]: Shifted mirrored wave.
    """
    return arr + arr[-2::-1]
