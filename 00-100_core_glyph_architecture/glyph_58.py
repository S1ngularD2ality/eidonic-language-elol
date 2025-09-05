def triad_split(arr):
    """
    Splits array into three equal substreams.

    Parameters:
        arr (List[int]): Symbol stream.

    Returns:
        List[List[int]]: Tri-folded split.
    """
    n = len(arr) // 3
    return [arr[:n], arr[n:2*n], arr[2*n:]]
