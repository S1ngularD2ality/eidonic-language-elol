def recursive_flip(arr):
    """
    Recursively reflects and flattens.

    Returns:
        List[int]
    """
    if not arr:
        return []
    return arr[::-1] + recursive_flip(arr[:-1])
