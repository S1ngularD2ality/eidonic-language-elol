def find_interrupts(arr):
    """
    Detects breaks in repeating symbol patterns.

    Parameters:
        arr (List[int]): Sequence.

    Returns:
        List[int]: Indices of interruption.
    """
    return [i for i in range(1, len(arr)) if arr[i] != arr[i-1]]
