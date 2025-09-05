def shift_inject(arr, offset):
    """
    Shifts all values by a symbolic offset.

    Parameters:
        arr (List[int]): Frame sequence.
        offset (int): Amount to shift.

    Returns:
        List[int]: Shifted array.
    """
    return [x + offset for x in arr]
