def path_signature(arr):
    """
    Generates symbolic path signature based on direction of change.

    Parameters:
        arr (List[int]): Navigational data.

    Returns:
        List[str]: Signature of movement ('U', 'D', 'S').
    """
    return ['U' if arr[i+1] > arr[i] else 'D' if arr[i+1] < arr[i] else 'S' for i in range(len(arr)-1)]
