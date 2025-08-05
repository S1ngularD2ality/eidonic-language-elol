def fork_split(arr):
    """
    Splits a path into two based on even/odd divergence.

    Parameters:
        arr (List[int]): Path stream.

    Returns:
        Tuple[List[int], List[int]]: Even and odd-indexed elements.
    """
    return arr[::2], arr[1::2]
