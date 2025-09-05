def is_mirror_balanced(arr):
    """
    Checks if array reads the same forward and backward.

    Parameters:
        arr (List[int]): Symbol sequence.

    Returns:
        bool: True if mirrored.
    """
    return arr == arr[::-1]
