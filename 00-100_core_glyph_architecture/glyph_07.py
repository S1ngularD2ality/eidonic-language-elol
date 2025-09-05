def symmetry_filter(arr):
    """
    Filters values that have symmetrical counterparts within the array.

    Parameters:
        arr (List[int]): The input list of integers.

    Returns:
        List[int]: Values that are reflected symmetrically across the center axis.
    """
    return [x for x in arr if -x in arr]
