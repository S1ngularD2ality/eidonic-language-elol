def normalize_path(arr):
    """
    Normalizes a symbolic path to a 0-based origin.

    Parameters:
        arr (List[int]): Path values.

    Returns:
        List[int]: Normalized path.
    """
    return [x - arr[0] for x in arr]
