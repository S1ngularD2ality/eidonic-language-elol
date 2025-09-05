def core_signature(arr):
    """
    Extracts middle third as symbolic signature.

    Parameters:
        arr (List[int]): Full signal.

    Returns:
        List[int]: Core slice.
    """
    n = len(arr)
    third = n // 3
    return arr[third:2*third]
