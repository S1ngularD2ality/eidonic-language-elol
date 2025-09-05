def mirrorlock_trace(arr):
    """
    Detects symmetrical mirrored sections.

    Parameters:
        arr (List[int]): Sequence.

    Returns:
        List[Tuple[int, int]]: Index pairs of symmetry.
    """
    return [(i, len(arr)-1-i) for i in range(len(arr)//2) if arr[i] == arr[len(arr)-1-i]]
