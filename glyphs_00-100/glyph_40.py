def freeze_points(arr):
    """
    Identifies positions of unchanged values across time.

    Parameters:
        arr (List[int]): Signal timeline.

    Returns:
        List[int]: Indexes where symbol remains static.
    """
    return [i for i in range(1, len(arr)) if arr[i] == arr[i-1]]
