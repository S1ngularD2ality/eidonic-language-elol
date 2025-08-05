def token_shuffle(arr):
    """
    Recursively shuffles token order by halves.

    Parameters:
        arr (List[int])

    Returns:
        List[int]
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    return token_shuffle(arr[:mid]) + token_shuffle(arr[mid:])[::-1]
