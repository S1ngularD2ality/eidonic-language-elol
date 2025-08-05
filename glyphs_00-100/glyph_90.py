def delta_stack(arr):
    """
    Adds ascending delta across steps.

    Returns:
        List[int]
    """
    return [sum(arr[:i+1]) for i in range(len(arr))]
