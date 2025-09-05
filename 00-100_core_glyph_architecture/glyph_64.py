def shift_carousel(arr, shift):
    """
    Rotates array by shift value.

    Parameters:
        arr (List[int]): Input.
        shift (int): Shift count.

    Returns:
        List[int]: Rotated array.
    """
    shift %= len(arr)
    return arr[-shift:] + arr[:-shift]
